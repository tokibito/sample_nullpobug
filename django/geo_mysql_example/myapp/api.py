from myapp.models import Shop

def get_shop_list(lat, lng):
    shop_queryset = Shop.objects.raw("""
SELECT
  *,
  (
    6371
    * acos(
      cos(radians(%%s))
      * cos(radians(latitude))
      * cos(radians(longitude) - radians(%%s))
      + sin(radians(%%s))
      * sin(radians(latitude)) 
    ) 
  ) AS distance 
FROM %(table)s 
HAVING distance < 1 
ORDER BY distance
""" % {'table': Shop._meta.db_table},
        [lat, lng, lat])
    return shop_queryset
