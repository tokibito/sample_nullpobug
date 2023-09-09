#!/usr/bin/env python
import os
import subprocess
from argparse import ArgumentParser
from pathlib import Path

import openai
from pydub import AudioSegment


def cmd_extractsound(args):
    """ffmpegでmp3抽出"""
    input_filepath = args.filepath
    p = Path(input_filepath)
    output_filepath = str(p.with_suffix(".mp3"))
    cmd = ["ffmpeg", "-i", input_filepath, "-ab", "256k", output_filepath]
    subprocess.run(cmd)


def cmd_splitchunks(args):
    input_filepath = args.filepath
    p = Path(input_filepath)
    audio = AudioSegment.from_mp3(input_filepath)

    # PyDub handles time in milliseconds
    milliseconds = args.chunk_seconds * 1000

    # ファイルをmillisecondsごとに分割
    chunks = [audio[i : i + milliseconds] for i in range(0, len(audio), milliseconds)]

    # 各チャンクを個別のファイルとして保存
    for idx, chunk in enumerate(chunks, 1):
        output_filepath = f"{p.with_suffix('')}_chunk{idx}{p.suffix}"
        chunk.export(output_filepath, format="mp3")


def cmd_processwhisper(args):
    """OpenAIのwhisperに送信してjsonで受け取る"""
    input_filepath = args.filepath
    p = Path(input_filepath)
    output_filepath = str(p.with_suffix(f".{args.response_format}"))
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        raise Exception("環境変数 OPENAI_API_KEY が未定義")
    openai.api_key = openai_api_key
    prompt = args.prompt
    with open(input_filepath, "rb") as input_file:
        transcript = openai.Audio.transcribe(
            "whisper-1", input_file, response_format=args.response_format, prompt=prompt
        )
    with open(output_filepath, "w") as fp:
        fp.write(str(transcript))


if __name__ == "__main__":
    parser = ArgumentParser(prog="OpenAI whisper client")
    subparsers = parser.add_subparsers(required=True)
    # extractsound command
    extractsound = subparsers.add_parser("extractsound", aliases=["es"])
    extractsound.add_argument("filepath")
    extractsound.set_defaults(func=cmd_extractsound)
    # splitchunks command
    splitchunks = subparsers.add_parser("splitchunks", aliases=["sc"])
    splitchunks.add_argument("filepath")
    splitchunks.add_argument("--chunk-seconds", type=int, default=60 * 10)
    splitchunks.set_defaults(func=cmd_splitchunks)
    # processwhisper command
    processwhisper = subparsers.add_parser("processwhisper", aliases=["pw"])
    processwhisper.add_argument("filepath")
    processwhisper.add_argument("prompt")
    processwhisper.add_argument("--response-format", default="srt")
    processwhisper.set_defaults(func=cmd_processwhisper)
    args = parser.parse_args()
    args.func(args)
