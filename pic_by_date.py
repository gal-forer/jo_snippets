import datetime
import pytz
def bubblesort(array):
    # we minus 1 because we are always comparing the current value with the next value
    lengthOfArray = len(array) - 1
    # numbe of rounds will be the total length - 1, for array with length 5, we will do 4 rounds: 0 and 1, 1 and 2, 2 and 3, 3 and 4.
    for i in range(lengthOfArray):
        # at each round, we compare the current j with the next value
        for j in range(lengthOfArray - i):
            # only swap their positions if left value < right value as we aim to move all the small values to the back
            if array[j][2] < array[j+1][2]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array.reverse()

str_1 = "photo.jpg, Warsaw, 2013-09-05 14:08:15\n" \
      "john.png, London, 2015-06-20 15:13:22\n" \
      "myFriends.png, Warsaw, 2013-09-05 14:07:13\n" \
      "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n" \
      "pisatower.jpg, Paris, 2015-07-22 23:59:59\n" \
      "BOB.jpg, London, 2015-08-05 00:02:03\n" \
      "notredame.png, Paris, 2015-09-01 12:00:00\n" \
      "me.jpg, Warsaw, 2013-09-06 15:40:22\n" \
      "a.png, Warsaw, 2016-02-13 13:33:50\n" \
      "b.jpg, Warsaw, 2016-01-02 15:12:22\n" \
      "c.jpg, Warsaw, 2016-01-02 14:34:30\n" \
      "d.jpg, Warsaw, 2016-01-02 15:15:01\n" \
      "e.png, Warsaw, 2016-01-02 09:49:09\n" \
      "f.png, Warsaw, 2016-01-02 10:55:32\n" \
      "g.jpg, Warsaw, 2016-02-29 22:13:11"

xx = str_1.split("\n")
cities = {}
photos = []
for x in xx:
    photos.append(x.split(","))
for photo in photos:
    photo[2] = datetime.datetime.strptime(photo[2], " %Y-%m-%d %H:%M:%S")
    timezone = pytz.timezone("UTC")
    # sets the timezone to the datetime object
    photo[2] = timezone.localize(photo[2])
    if photo[1] not in cities:
        cities[photo[1]]=photo[1]
        cities[photo[1]]=list()
    cities[photo[1]].append(photo)
for city in cities:
    bubblesort(cities[city])
    idx = 1
    for photo in cities[city]:

        for p in photos:
            if photo[0]==p[0]:
                str_t=photo[1]+str(idx)+'.'+photo[0].split(".")[1]
                p[0] = str_t
                idx += 1
for photo in photos:
    print photo[0]+','+photo[2].strftime("%Y/%m/%d %H:%M")
print(photos)