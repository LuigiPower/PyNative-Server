#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pynative.pynative import PyNative
from pynative.views import *

pygna = PyNative()

@pygna.flask.route('/image/<imagename>.<imagetype>')
def getImage(imagename, imagetype):
	print "hey %s %s" % (imagename, imagetype)
	return pygna.getImage(imagename + "." + imagetype, imagetype)

# @pygna.flask.route('/icon/<imagename>')
# def getImage(imagename, imagetype):
# 	return pygna.getImage(imagename, "icon")


@pygna.flask.route('/<requestedScreenname>', methods=['GET', 'POST'])
def interfaceBuilder(requestedScreenname):
    screen = Screen()

    loremipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque odio velit, vehicula et dolor sit amet, dapibus commodo urna. Integer congue lacinia magna, quis sodales arcu vulputate sed. Duis nec risus vitae quam pharetra faucibus. Mauris auctor quam at pretium interdum. Vivamus tempus dapibus purus quis pellentesque. Quisque at semper tortor. Sed pretium elit sit amet condimentum semper.

Pellentesque dignissim nunc id dolor sodales, sit amet varius mi gravida. Quisque iaculis aliquam ligula eget vestibulum. Donec scelerisque turpis id eros maximus, euismod egestas arcu rutrum. Vestibulum quis eros at arcu varius porttitor vehicula et nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In hac habitasse platea dictumst. Cras malesuada nunc euismod mollis pretium. Nulla faucibus sodales libero eget tristique. Proin nec vestibulum risus, nec vulputate turpis. Duis vestibulum metus mauris, nec molestie lectus ornare tempus. Nam nec consequat enim. Maecenas non nunc et eros commodo ultricies sed vel ex. Praesent luctus placerat ante eu rutrum. Nam lacus lacus, maximus a quam facilisis, rhoncus porttitor sem.

Proin lacinia lorem sed lorem ornare vehicula. Sed rhoncus, ipsum vel euismod facilisis, sem massa pretium mi, et mollis nibh magna id justo. Cras quis urna gravida, lobortis erat non, finibus lectus. Etiam eu eros dignissim, lobortis nibh sed, posuere mauris. Aliquam eu porta diam, sit amet dapibus nulla. Nunc porttitor, risus quis sollicitudin maximus, orci enim lacinia leo, quis venenatis lectus felis ut dolor. Suspendisse vel velit pharetra, iaculis ligula sed, molestie velit. Pellentesque accumsan lacus nec dui luctus, a commodo lacus ultricies. Aenean tristique quam erat, ac eleifend est imperdiet vitae.

In molestie tellus vel felis pellentesque mollis. Proin convallis dui et urna porta laoreet. Sed sagittis aliquet finibus. Nulla id leo eros. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec pulvinar, ipsum in vehicula varius, sapien urna iaculis felis, id gravida tellus mauris sed arcu. Praesent molestie sapien sit amet est bibendum convallis. Vivamus aliquet id quam sed pellentesque. Quisque dignissim volutpat dolor, eu condimentum risus fermentum vitae. Nam urna odio, sollicitudin a gravida in, condimentum at magna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer vitae consequat nisl. Nunc tellus quam, facilisis fermentum metus ut, mattis vestibulum nunc. Curabitur at ipsum et augue consequat lacinia.

Sed sit amet venenatis ligula, eu sollicitudin metus. Integer facilisis felis eget est hendrerit mollis. Mauris euismod tincidunt ligula, at volutpat ex feugiat vitae. Donec eu erat ligula. Suspendisse laoreet enim a orci congue, in molestie neque ornare. Etiam dolor est, rutrum eleifend maximus vel, dapibus ac leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi venenatis justo sit amet odio egestas imperdiet. Phasellus dapibus id felis a feugiat. In vulputate pharetra libero. Suspendisse elementum a lacus id dignissim.
    """
    data_radiobutton = [
    	{"label": "Miao", "value": "Miao"},
    	{"label": "Miao2", "value": "Miao2"},
    	{"label": "Miao3", "value": "Miao3"},
    ]
    imgpath = "/image/miaomiao.png"
    ckb = Checkbox("Miao")
    rdb = RadioButton("")
    rdb.set_data(data_radiobutton) 
    img = ImageView(imgpath)

    screen.add_view(TextView("Ciao Mondo"))
    screen.add_view(TextView(loremipsum))
    screen.add_view(Button("Avanti"))
    screen.add_view(ckb)
    screen.add_view(rdb)
    screen.add_view(img)
    return pygna.render(screen)

if __name__ == "__main__":
    pygna.flask.run(host="0.0.0.0", debug=True)
