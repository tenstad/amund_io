from django.http import JsonResponse
from django.views.generic import TemplateView
from PIL import Image
from io import BytesIO
from base64 import b64decode
import numpy as np
import binascii
import os

class DemoView(TemplateView):
    template_name = 'numclass/demo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'range10': list(range(10)),
        })
        return context


def predict(request):
    try:
        raw = request.GET.get('image').split('base64,')[1]
        bts = BytesIO(b64decode(raw))
        img = Image.open(bts)
        rawimg = img

        img = img.convert('RGB')
        img = img.resize((16, 16))

        net = Net.load('trained_weights_200px.npy')
        output = net.run(read_image(img))
        index = list(output).index(max(output))

        path = os.getcwd() + '\\..\\numclass_images/%r/' % index
        files = os.listdir(path)
        if not files:
            next = 0
        else:
            next = max([int(a.split('.')[0]) for a in files]) + 1
        rawimg.save(path + '%r.png' % next)

    except (binascii.Error, OSError):
        output = [0] * 10

    return JsonResponse({
        'probabilities': list(output),
    })

def sigmoid(x, deriv=False):
    if deriv:
        return x * (1-x)
    return 1 / (1+np.exp(-x))

class Net:
    def __init__(self, layer_sizes, activation=sigmoid):
        self.layer_sizes = layer_sizes
        self.activation = activation
        self.weights = np.array([2 * np.random.rand(layer_sizes[i], layer_sizes[i+1]) - 1 for i in range(len(layer_sizes)-1)])
        self.layers = None

    def __len__(self):
        return len(self.layer_sizes)

    @staticmethod
    def load(filename):
        weights = np.load(filename)
        layer_sizes = [len(a) for a in weights]
        layer_sizes.append(len(weights[-1][0]))
        net = Net(layer_sizes)
        net.weights = weights
        return net

    def run(self, x):
        self.layers = [None for _ in self.layer_sizes]
        self.layers[0] = np.array(x)
        for i in range(len(self)-1):
            x = self.activation(np.dot(x, self.weights[i]))
            self.layers[i+1] = x
        return x

def read_image(img, resize=None):
    img = img.convert('RGB')

    if resize:
        img = img.resize(resize, Image.ANTIALIAS)

    values = []

    for j in range(img.size[1]):
        for i in range(img.size[0]):
            values.append(sum(img.getpixel((i, j))) / (3 * 255))

    return values