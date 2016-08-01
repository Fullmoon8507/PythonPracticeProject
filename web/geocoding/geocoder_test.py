import geocoder

n = "東京スカイツリー"
a = "東京都墨田区押上１丁目１−２"

g = geocoder.google(a)
print(a, "-->", g.latlng)

g = geocoder.google(n)
print(n, "-->", g.latlng)