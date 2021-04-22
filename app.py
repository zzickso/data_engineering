from flask import Flask , render_template ,request ,redirect
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO, StringIO #그래프를 이미지로 저장하기 위해 필요한 변환 라이브러리

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("index.html", data="KIM")

@app.route('/fig/<int:mean>_<int:var>')
def fig(mean, var):
    plt.figure(figsize=(4,3))
    xs = np.random.normal(mean, var, 100)
    ys = np.random.normal(mean, var, 100)
    plt.scatter(xs, ys, s=100, marker='h', color='red', alpha=0.3)
    
    img = BytesIO()
    plt.savefig(img, format='png', dpi =200)
    img.seek(0)

    #print(xs)
    return "success"

@app.route('/normal/<m_v>')
def normal(m_v):
    m, v = m_v.split('_')
    m, v = int(m), int(v)
    return render_template("random_gen.html", mean=m, var= v, width =200, height=200)


if __name__ == '__main__':
  app.run()