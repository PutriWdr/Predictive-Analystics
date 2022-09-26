{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNnN2pQN6BgXr8SIJ8KTFiT",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/PutriWdr/Predictive-Analystics/blob/main/predictive_analytics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Yb8txNKMZfSF"
      },
      "outputs": [],
      "source": [
        "# install kagglee\n",
        "!pip install -q kaggle\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Nama: Putri Wulandari\n",
        "\n",
        "ID: M495Y1038\n",
        "\n",
        "Kelas: Machine Learning dan Terapan\n",
        "\n",
        "Laporan Proyek Predictive Analytics"
      ],
      "metadata": {
        "id": "LaHUVkf_ZjWg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Menyambungkan dengan *kaggle*\n",
        "*uploaddd kaggle.json*"
      ],
      "metadata": {
        "id": "_fq82iyYDTUn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 93
        },
        "id": "HjlIqgKZ888L",
        "outputId": "f48e6ba8-5ed3-4a7f-fdbb-7a6ed2ce951a"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-6781187b-f2ba-42c4-9179-b706cc85ed0d\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-6781187b-f2ba-42c4-9179-b706cc85ed0d\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving kaggle.json to kaggle.json\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'kaggle.json': b'{\"username\":\"putriwulandari12345\",\"key\":\"983467ba58df84cfd8fd9df601c25432\"}'}"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Membuat *direktory *\n",
        " *make directory dan change permissionnn*"
      ],
      "metadata": {
        "id": "wUtobo6QDvZ4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "!mkdir -p ~/.kaggle\n",
        "!cp kaggle.json ~/.kaggle/\n",
        "!chmod 600 ~/.kaggle/kaggle.json\n",
        "!ls ~/.kaggle"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ouLzhbvd89GZ",
        "outputId": "4f200879-1701-465a-80fb-9c4e401f9221"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "kaggle.json\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Mendownload dataset"
      ],
      "metadata": {
        "id": "bomAwyrL-H-1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# download dataset,\n",
        "!kaggle datasets download -d yasserh/breast-cancer-dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U39UsRqM-L9K",
        "outputId": "89c5b870-1d27-4ab8-89a1-dbb3dc9bf1ad"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading breast-cancer-dataset.zip to /content\n",
            "\r  0% 0.00/48.6k [00:00<?, ?B/s]\n",
            "\r100% 48.6k/48.6k [00:00<00:00, 48.9MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Mengimport zip file"
      ],
      "metadata": {
        "id": "I6iiaPa3-pls"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from zipfile import ZipFile\n",
        "file_name = \"/content/breast-cancer-dataset.zip\"\n",
        "\n",
        "with ZipFile(file_name,'r') as zip:\n",
        "  zip.extractall()\n",
        "  print(\"done\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L_TFeQFP-c8V",
        "outputId": "62aa1165-14f5-4ae3-c01c-a28ecd3a39dc"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "done\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Mengimpor pustaka atau modul python"
      ],
      "metadata": {
        "id": "ZMCr6Aqs-8Ed"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "%matplotlib inline\n",
        "import seaborn as sns\n",
        "\n",
        "from sklearn.utils import resample \n",
        "from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder\n",
        "\n",
        "# Untuk pembuatan model \n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.metrics import accuracy_score, classification_report\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import accuracy_score, confusion_matrix"
      ],
      "metadata": {
        "id": "e4mRB0_0_Dq_"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Data Understanding"
      ],
      "metadata": {
        "id": "jVafPKFX_Jmy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Memuat data sebuah dataframe menggunakan pandas"
      ],
      "metadata": {
        "id": "7VbU128p_R-4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "url = '/content/breast-cancer.csv'\n",
        "dt = pd.read_csv(url)\n",
        "dt"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 505
        },
        "id": "BgkWGu___ONt",
        "outputId": "dc659c91-5c7a-4133-ad27-28e28460feb3"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           id diagnosis  radius_mean  texture_mean  perimeter_mean  area_mean  \\\n",
              "0      842302         M        17.99         10.38          122.80     1001.0   \n",
              "1      842517         M        20.57         17.77          132.90     1326.0   \n",
              "2    84300903         M        19.69         21.25          130.00     1203.0   \n",
              "3    84348301         M        11.42         20.38           77.58      386.1   \n",
              "4    84358402         M        20.29         14.34          135.10     1297.0   \n",
              "..        ...       ...          ...           ...             ...        ...   \n",
              "564    926424         M        21.56         22.39          142.00     1479.0   \n",
              "565    926682         M        20.13         28.25          131.20     1261.0   \n",
              "566    926954         M        16.60         28.08          108.30      858.1   \n",
              "567    927241         M        20.60         29.33          140.10     1265.0   \n",
              "568     92751         B         7.76         24.54           47.92      181.0   \n",
              "\n",
              "     smoothness_mean  compactness_mean  concavity_mean  concave points_mean  \\\n",
              "0            0.11840           0.27760         0.30010              0.14710   \n",
              "1            0.08474           0.07864         0.08690              0.07017   \n",
              "2            0.10960           0.15990         0.19740              0.12790   \n",
              "3            0.14250           0.28390         0.24140              0.10520   \n",
              "4            0.10030           0.13280         0.19800              0.10430   \n",
              "..               ...               ...             ...                  ...   \n",
              "564          0.11100           0.11590         0.24390              0.13890   \n",
              "565          0.09780           0.10340         0.14400              0.09791   \n",
              "566          0.08455           0.10230         0.09251              0.05302   \n",
              "567          0.11780           0.27700         0.35140              0.15200   \n",
              "568          0.05263           0.04362         0.00000              0.00000   \n",
              "\n",
              "     ...  radius_worst  texture_worst  perimeter_worst  area_worst  \\\n",
              "0    ...        25.380          17.33           184.60      2019.0   \n",
              "1    ...        24.990          23.41           158.80      1956.0   \n",
              "2    ...        23.570          25.53           152.50      1709.0   \n",
              "3    ...        14.910          26.50            98.87       567.7   \n",
              "4    ...        22.540          16.67           152.20      1575.0   \n",
              "..   ...           ...            ...              ...         ...   \n",
              "564  ...        25.450          26.40           166.10      2027.0   \n",
              "565  ...        23.690          38.25           155.00      1731.0   \n",
              "566  ...        18.980          34.12           126.70      1124.0   \n",
              "567  ...        25.740          39.42           184.60      1821.0   \n",
              "568  ...         9.456          30.37            59.16       268.6   \n",
              "\n",
              "     smoothness_worst  compactness_worst  concavity_worst  \\\n",
              "0             0.16220            0.66560           0.7119   \n",
              "1             0.12380            0.18660           0.2416   \n",
              "2             0.14440            0.42450           0.4504   \n",
              "3             0.20980            0.86630           0.6869   \n",
              "4             0.13740            0.20500           0.4000   \n",
              "..                ...                ...              ...   \n",
              "564           0.14100            0.21130           0.4107   \n",
              "565           0.11660            0.19220           0.3215   \n",
              "566           0.11390            0.30940           0.3403   \n",
              "567           0.16500            0.86810           0.9387   \n",
              "568           0.08996            0.06444           0.0000   \n",
              "\n",
              "     concave points_worst  symmetry_worst  fractal_dimension_worst  \n",
              "0                  0.2654          0.4601                  0.11890  \n",
              "1                  0.1860          0.2750                  0.08902  \n",
              "2                  0.2430          0.3613                  0.08758  \n",
              "3                  0.2575          0.6638                  0.17300  \n",
              "4                  0.1625          0.2364                  0.07678  \n",
              "..                    ...             ...                      ...  \n",
              "564                0.2216          0.2060                  0.07115  \n",
              "565                0.1628          0.2572                  0.06637  \n",
              "566                0.1418          0.2218                  0.07820  \n",
              "567                0.2650          0.4087                  0.12400  \n",
              "568                0.0000          0.2871                  0.07039  \n",
              "\n",
              "[569 rows x 32 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-d3ccda2d-9736-48f0-a30b-dc974da59e70\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>diagnosis</th>\n",
              "      <th>radius_mean</th>\n",
              "      <th>texture_mean</th>\n",
              "      <th>perimeter_mean</th>\n",
              "      <th>area_mean</th>\n",
              "      <th>smoothness_mean</th>\n",
              "      <th>compactness_mean</th>\n",
              "      <th>concavity_mean</th>\n",
              "      <th>concave points_mean</th>\n",
              "      <th>...</th>\n",
              "      <th>radius_worst</th>\n",
              "      <th>texture_worst</th>\n",
              "      <th>perimeter_worst</th>\n",
              "      <th>area_worst</th>\n",
              "      <th>smoothness_worst</th>\n",
              "      <th>compactness_worst</th>\n",
              "      <th>concavity_worst</th>\n",
              "      <th>concave points_worst</th>\n",
              "      <th>symmetry_worst</th>\n",
              "      <th>fractal_dimension_worst</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>842302</td>\n",
              "      <td>M</td>\n",
              "      <td>17.99</td>\n",
              "      <td>10.38</td>\n",
              "      <td>122.80</td>\n",
              "      <td>1001.0</td>\n",
              "      <td>0.11840</td>\n",
              "      <td>0.27760</td>\n",
              "      <td>0.30010</td>\n",
              "      <td>0.14710</td>\n",
              "      <td>...</td>\n",
              "      <td>25.380</td>\n",
              "      <td>17.33</td>\n",
              "      <td>184.60</td>\n",
              "      <td>2019.0</td>\n",
              "      <td>0.16220</td>\n",
              "      <td>0.66560</td>\n",
              "      <td>0.7119</td>\n",
              "      <td>0.2654</td>\n",
              "      <td>0.4601</td>\n",
              "      <td>0.11890</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>842517</td>\n",
              "      <td>M</td>\n",
              "      <td>20.57</td>\n",
              "      <td>17.77</td>\n",
              "      <td>132.90</td>\n",
              "      <td>1326.0</td>\n",
              "      <td>0.08474</td>\n",
              "      <td>0.07864</td>\n",
              "      <td>0.08690</td>\n",
              "      <td>0.07017</td>\n",
              "      <td>...</td>\n",
              "      <td>24.990</td>\n",
              "      <td>23.41</td>\n",
              "      <td>158.80</td>\n",
              "      <td>1956.0</td>\n",
              "      <td>0.12380</td>\n",
              "      <td>0.18660</td>\n",
              "      <td>0.2416</td>\n",
              "      <td>0.1860</td>\n",
              "      <td>0.2750</td>\n",
              "      <td>0.08902</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>84300903</td>\n",
              "      <td>M</td>\n",
              "      <td>19.69</td>\n",
              "      <td>21.25</td>\n",
              "      <td>130.00</td>\n",
              "      <td>1203.0</td>\n",
              "      <td>0.10960</td>\n",
              "      <td>0.15990</td>\n",
              "      <td>0.19740</td>\n",
              "      <td>0.12790</td>\n",
              "      <td>...</td>\n",
              "      <td>23.570</td>\n",
              "      <td>25.53</td>\n",
              "      <td>152.50</td>\n",
              "      <td>1709.0</td>\n",
              "      <td>0.14440</td>\n",
              "      <td>0.42450</td>\n",
              "      <td>0.4504</td>\n",
              "      <td>0.2430</td>\n",
              "      <td>0.3613</td>\n",
              "      <td>0.08758</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>84348301</td>\n",
              "      <td>M</td>\n",
              "      <td>11.42</td>\n",
              "      <td>20.38</td>\n",
              "      <td>77.58</td>\n",
              "      <td>386.1</td>\n",
              "      <td>0.14250</td>\n",
              "      <td>0.28390</td>\n",
              "      <td>0.24140</td>\n",
              "      <td>0.10520</td>\n",
              "      <td>...</td>\n",
              "      <td>14.910</td>\n",
              "      <td>26.50</td>\n",
              "      <td>98.87</td>\n",
              "      <td>567.7</td>\n",
              "      <td>0.20980</td>\n",
              "      <td>0.86630</td>\n",
              "      <td>0.6869</td>\n",
              "      <td>0.2575</td>\n",
              "      <td>0.6638</td>\n",
              "      <td>0.17300</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>84358402</td>\n",
              "      <td>M</td>\n",
              "      <td>20.29</td>\n",
              "      <td>14.34</td>\n",
              "      <td>135.10</td>\n",
              "      <td>1297.0</td>\n",
              "      <td>0.10030</td>\n",
              "      <td>0.13280</td>\n",
              "      <td>0.19800</td>\n",
              "      <td>0.10430</td>\n",
              "      <td>...</td>\n",
              "      <td>22.540</td>\n",
              "      <td>16.67</td>\n",
              "      <td>152.20</td>\n",
              "      <td>1575.0</td>\n",
              "      <td>0.13740</td>\n",
              "      <td>0.20500</td>\n",
              "      <td>0.4000</td>\n",
              "      <td>0.1625</td>\n",
              "      <td>0.2364</td>\n",
              "      <td>0.07678</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>564</th>\n",
              "      <td>926424</td>\n",
              "      <td>M</td>\n",
              "      <td>21.56</td>\n",
              "      <td>22.39</td>\n",
              "      <td>142.00</td>\n",
              "      <td>1479.0</td>\n",
              "      <td>0.11100</td>\n",
              "      <td>0.11590</td>\n",
              "      <td>0.24390</td>\n",
              "      <td>0.13890</td>\n",
              "      <td>...</td>\n",
              "      <td>25.450</td>\n",
              "      <td>26.40</td>\n",
              "      <td>166.10</td>\n",
              "      <td>2027.0</td>\n",
              "      <td>0.14100</td>\n",
              "      <td>0.21130</td>\n",
              "      <td>0.4107</td>\n",
              "      <td>0.2216</td>\n",
              "      <td>0.2060</td>\n",
              "      <td>0.07115</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>565</th>\n",
              "      <td>926682</td>\n",
              "      <td>M</td>\n",
              "      <td>20.13</td>\n",
              "      <td>28.25</td>\n",
              "      <td>131.20</td>\n",
              "      <td>1261.0</td>\n",
              "      <td>0.09780</td>\n",
              "      <td>0.10340</td>\n",
              "      <td>0.14400</td>\n",
              "      <td>0.09791</td>\n",
              "      <td>...</td>\n",
              "      <td>23.690</td>\n",
              "      <td>38.25</td>\n",
              "      <td>155.00</td>\n",
              "      <td>1731.0</td>\n",
              "      <td>0.11660</td>\n",
              "      <td>0.19220</td>\n",
              "      <td>0.3215</td>\n",
              "      <td>0.1628</td>\n",
              "      <td>0.2572</td>\n",
              "      <td>0.06637</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>566</th>\n",
              "      <td>926954</td>\n",
              "      <td>M</td>\n",
              "      <td>16.60</td>\n",
              "      <td>28.08</td>\n",
              "      <td>108.30</td>\n",
              "      <td>858.1</td>\n",
              "      <td>0.08455</td>\n",
              "      <td>0.10230</td>\n",
              "      <td>0.09251</td>\n",
              "      <td>0.05302</td>\n",
              "      <td>...</td>\n",
              "      <td>18.980</td>\n",
              "      <td>34.12</td>\n",
              "      <td>126.70</td>\n",
              "      <td>1124.0</td>\n",
              "      <td>0.11390</td>\n",
              "      <td>0.30940</td>\n",
              "      <td>0.3403</td>\n",
              "      <td>0.1418</td>\n",
              "      <td>0.2218</td>\n",
              "      <td>0.07820</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>567</th>\n",
              "      <td>927241</td>\n",
              "      <td>M</td>\n",
              "      <td>20.60</td>\n",
              "      <td>29.33</td>\n",
              "      <td>140.10</td>\n",
              "      <td>1265.0</td>\n",
              "      <td>0.11780</td>\n",
              "      <td>0.27700</td>\n",
              "      <td>0.35140</td>\n",
              "      <td>0.15200</td>\n",
              "      <td>...</td>\n",
              "      <td>25.740</td>\n",
              "      <td>39.42</td>\n",
              "      <td>184.60</td>\n",
              "      <td>1821.0</td>\n",
              "      <td>0.16500</td>\n",
              "      <td>0.86810</td>\n",
              "      <td>0.9387</td>\n",
              "      <td>0.2650</td>\n",
              "      <td>0.4087</td>\n",
              "      <td>0.12400</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>568</th>\n",
              "      <td>92751</td>\n",
              "      <td>B</td>\n",
              "      <td>7.76</td>\n",
              "      <td>24.54</td>\n",
              "      <td>47.92</td>\n",
              "      <td>181.0</td>\n",
              "      <td>0.05263</td>\n",
              "      <td>0.04362</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>...</td>\n",
              "      <td>9.456</td>\n",
              "      <td>30.37</td>\n",
              "      <td>59.16</td>\n",
              "      <td>268.6</td>\n",
              "      <td>0.08996</td>\n",
              "      <td>0.06444</td>\n",
              "      <td>0.0000</td>\n",
              "      <td>0.0000</td>\n",
              "      <td>0.2871</td>\n",
              "      <td>0.07039</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>569 rows × 32 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d3ccda2d-9736-48f0-a30b-dc974da59e70')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-d3ccda2d-9736-48f0-a30b-dc974da59e70 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-d3ccda2d-9736-48f0-a30b-dc974da59e70');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tabel 1. Dataframe\n",
        "Pada tabel di atas menunjukkan hasil data menggunakan pandas."
      ],
      "metadata": {
        "id": "o5XIaBOpI97Y"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Memuat type atau info kolom  pada dataset"
      ],
      "metadata": {
        "id": "d7W5qHXv_sWU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dt.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MvOnQ6DA_1AU",
        "outputId": "64c343f3-6b54-4681-8222-c4e319735b40"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 569 entries, 0 to 568\n",
            "Data columns (total 32 columns):\n",
            " #   Column                   Non-Null Count  Dtype  \n",
            "---  ------                   --------------  -----  \n",
            " 0   id                       569 non-null    int64  \n",
            " 1   diagnosis                569 non-null    object \n",
            " 2   radius_mean              569 non-null    float64\n",
            " 3   texture_mean             569 non-null    float64\n",
            " 4   perimeter_mean           569 non-null    float64\n",
            " 5   area_mean                569 non-null    float64\n",
            " 6   smoothness_mean          569 non-null    float64\n",
            " 7   compactness_mean         569 non-null    float64\n",
            " 8   concavity_mean           569 non-null    float64\n",
            " 9   concave points_mean      569 non-null    float64\n",
            " 10  symmetry_mean            569 non-null    float64\n",
            " 11  fractal_dimension_mean   569 non-null    float64\n",
            " 12  radius_se                569 non-null    float64\n",
            " 13  texture_se               569 non-null    float64\n",
            " 14  perimeter_se             569 non-null    float64\n",
            " 15  area_se                  569 non-null    float64\n",
            " 16  smoothness_se            569 non-null    float64\n",
            " 17  compactness_se           569 non-null    float64\n",
            " 18  concavity_se             569 non-null    float64\n",
            " 19  concave points_se        569 non-null    float64\n",
            " 20  symmetry_se              569 non-null    float64\n",
            " 21  fractal_dimension_se     569 non-null    float64\n",
            " 22  radius_worst             569 non-null    float64\n",
            " 23  texture_worst            569 non-null    float64\n",
            " 24  perimeter_worst          569 non-null    float64\n",
            " 25  area_worst               569 non-null    float64\n",
            " 26  smoothness_worst         569 non-null    float64\n",
            " 27  compactness_worst        569 non-null    float64\n",
            " 28  concavity_worst          569 non-null    float64\n",
            " 29  concave points_worst     569 non-null    float64\n",
            " 30  symmetry_worst           569 non-null    float64\n",
            " 31  fractal_dimension_worst  569 non-null    float64\n",
            "dtypes: float64(30), int64(1), object(1)\n",
            "memory usage: 142.4+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Menghitung jumlah data kosong pada setiap kolom-kolom"
      ],
      "metadata": {
        "id": "uoWupgZ3LhnP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "dt.isna().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eFcMpBJV__Wb",
        "outputId": "e7a95f76-64ac-4243-f577-b257e495e738"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "id                         0\n",
              "diagnosis                  0\n",
              "radius_mean                0\n",
              "texture_mean               0\n",
              "perimeter_mean             0\n",
              "area_mean                  0\n",
              "smoothness_mean            0\n",
              "compactness_mean           0\n",
              "concavity_mean             0\n",
              "concave points_mean        0\n",
              "symmetry_mean              0\n",
              "fractal_dimension_mean     0\n",
              "radius_se                  0\n",
              "texture_se                 0\n",
              "perimeter_se               0\n",
              "area_se                    0\n",
              "smoothness_se              0\n",
              "compactness_se             0\n",
              "concavity_se               0\n",
              "concave points_se          0\n",
              "symmetry_se                0\n",
              "fractal_dimension_se       0\n",
              "radius_worst               0\n",
              "texture_worst              0\n",
              "perimeter_worst            0\n",
              "area_worst                 0\n",
              "smoothness_worst           0\n",
              "compactness_worst          0\n",
              "concavity_worst            0\n",
              "concave points_worst       0\n",
              "symmetry_worst             0\n",
              "fractal_dimension_worst    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Memuat ukuran-ukuran shape pada dataframe"
      ],
      "metadata": {
        "id": "D0OnNbcpEKYy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "dt.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XZchDxCb__sp",
        "outputId": "e2cf130c-a423-4d50-87cf-3a685c9e3939"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(569, 32)"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " Menghapus kolom yang tidak dibutuhkan"
      ],
      "metadata": {
        "id": "bdEkfL4hEHgT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "dt.drop(['id'], axis=1, inplace=True)"
      ],
      "metadata": {
        "id": "BF5lDz9lAQvY"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Memuat hitungan rata-rata dan lainnyaa pada variabel data"
      ],
      "metadata": {
        "id": "UFVEvfVbEERL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        " \n",
        "dt.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 411
        },
        "id": "SdHvV-2sAdf-",
        "outputId": "098a9c26-2357-4dbf-f159-c3e356990177"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       radius_mean  texture_mean  perimeter_mean    area_mean  \\\n",
              "count   569.000000    569.000000      569.000000   569.000000   \n",
              "mean     14.127292     19.289649       91.969033   654.889104   \n",
              "std       3.524049      4.301036       24.298981   351.914129   \n",
              "min       6.981000      9.710000       43.790000   143.500000   \n",
              "25%      11.700000     16.170000       75.170000   420.300000   \n",
              "50%      13.370000     18.840000       86.240000   551.100000   \n",
              "75%      15.780000     21.800000      104.100000   782.700000   \n",
              "max      28.110000     39.280000      188.500000  2501.000000   \n",
              "\n",
              "       smoothness_mean  compactness_mean  concavity_mean  concave points_mean  \\\n",
              "count       569.000000        569.000000      569.000000           569.000000   \n",
              "mean          0.096360          0.104341        0.088799             0.048919   \n",
              "std           0.014064          0.052813        0.079720             0.038803   \n",
              "min           0.052630          0.019380        0.000000             0.000000   \n",
              "25%           0.086370          0.064920        0.029560             0.020310   \n",
              "50%           0.095870          0.092630        0.061540             0.033500   \n",
              "75%           0.105300          0.130400        0.130700             0.074000   \n",
              "max           0.163400          0.345400        0.426800             0.201200   \n",
              "\n",
              "       symmetry_mean  fractal_dimension_mean  ...  radius_worst  \\\n",
              "count     569.000000              569.000000  ...    569.000000   \n",
              "mean        0.181162                0.062798  ...     16.269190   \n",
              "std         0.027414                0.007060  ...      4.833242   \n",
              "min         0.106000                0.049960  ...      7.930000   \n",
              "25%         0.161900                0.057700  ...     13.010000   \n",
              "50%         0.179200                0.061540  ...     14.970000   \n",
              "75%         0.195700                0.066120  ...     18.790000   \n",
              "max         0.304000                0.097440  ...     36.040000   \n",
              "\n",
              "       texture_worst  perimeter_worst   area_worst  smoothness_worst  \\\n",
              "count     569.000000       569.000000   569.000000        569.000000   \n",
              "mean       25.677223       107.261213   880.583128          0.132369   \n",
              "std         6.146258        33.602542   569.356993          0.022832   \n",
              "min        12.020000        50.410000   185.200000          0.071170   \n",
              "25%        21.080000        84.110000   515.300000          0.116600   \n",
              "50%        25.410000        97.660000   686.500000          0.131300   \n",
              "75%        29.720000       125.400000  1084.000000          0.146000   \n",
              "max        49.540000       251.200000  4254.000000          0.222600   \n",
              "\n",
              "       compactness_worst  concavity_worst  concave points_worst  \\\n",
              "count         569.000000       569.000000            569.000000   \n",
              "mean            0.254265         0.272188              0.114606   \n",
              "std             0.157336         0.208624              0.065732   \n",
              "min             0.027290         0.000000              0.000000   \n",
              "25%             0.147200         0.114500              0.064930   \n",
              "50%             0.211900         0.226700              0.099930   \n",
              "75%             0.339100         0.382900              0.161400   \n",
              "max             1.058000         1.252000              0.291000   \n",
              "\n",
              "       symmetry_worst  fractal_dimension_worst  \n",
              "count      569.000000               569.000000  \n",
              "mean         0.290076                 0.083946  \n",
              "std          0.061867                 0.018061  \n",
              "min          0.156500                 0.055040  \n",
              "25%          0.250400                 0.071460  \n",
              "50%          0.282200                 0.080040  \n",
              "75%          0.317900                 0.092080  \n",
              "max          0.663800                 0.207500  \n",
              "\n",
              "[8 rows x 30 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-18ef018c-3eff-4e50-b5b0-c8ad7db8b6c9\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>radius_mean</th>\n",
              "      <th>texture_mean</th>\n",
              "      <th>perimeter_mean</th>\n",
              "      <th>area_mean</th>\n",
              "      <th>smoothness_mean</th>\n",
              "      <th>compactness_mean</th>\n",
              "      <th>concavity_mean</th>\n",
              "      <th>concave points_mean</th>\n",
              "      <th>symmetry_mean</th>\n",
              "      <th>fractal_dimension_mean</th>\n",
              "      <th>...</th>\n",
              "      <th>radius_worst</th>\n",
              "      <th>texture_worst</th>\n",
              "      <th>perimeter_worst</th>\n",
              "      <th>area_worst</th>\n",
              "      <th>smoothness_worst</th>\n",
              "      <th>compactness_worst</th>\n",
              "      <th>concavity_worst</th>\n",
              "      <th>concave points_worst</th>\n",
              "      <th>symmetry_worst</th>\n",
              "      <th>fractal_dimension_worst</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>...</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "      <td>569.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>14.127292</td>\n",
              "      <td>19.289649</td>\n",
              "      <td>91.969033</td>\n",
              "      <td>654.889104</td>\n",
              "      <td>0.096360</td>\n",
              "      <td>0.104341</td>\n",
              "      <td>0.088799</td>\n",
              "      <td>0.048919</td>\n",
              "      <td>0.181162</td>\n",
              "      <td>0.062798</td>\n",
              "      <td>...</td>\n",
              "      <td>16.269190</td>\n",
              "      <td>25.677223</td>\n",
              "      <td>107.261213</td>\n",
              "      <td>880.583128</td>\n",
              "      <td>0.132369</td>\n",
              "      <td>0.254265</td>\n",
              "      <td>0.272188</td>\n",
              "      <td>0.114606</td>\n",
              "      <td>0.290076</td>\n",
              "      <td>0.083946</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>3.524049</td>\n",
              "      <td>4.301036</td>\n",
              "      <td>24.298981</td>\n",
              "      <td>351.914129</td>\n",
              "      <td>0.014064</td>\n",
              "      <td>0.052813</td>\n",
              "      <td>0.079720</td>\n",
              "      <td>0.038803</td>\n",
              "      <td>0.027414</td>\n",
              "      <td>0.007060</td>\n",
              "      <td>...</td>\n",
              "      <td>4.833242</td>\n",
              "      <td>6.146258</td>\n",
              "      <td>33.602542</td>\n",
              "      <td>569.356993</td>\n",
              "      <td>0.022832</td>\n",
              "      <td>0.157336</td>\n",
              "      <td>0.208624</td>\n",
              "      <td>0.065732</td>\n",
              "      <td>0.061867</td>\n",
              "      <td>0.018061</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>6.981000</td>\n",
              "      <td>9.710000</td>\n",
              "      <td>43.790000</td>\n",
              "      <td>143.500000</td>\n",
              "      <td>0.052630</td>\n",
              "      <td>0.019380</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.106000</td>\n",
              "      <td>0.049960</td>\n",
              "      <td>...</td>\n",
              "      <td>7.930000</td>\n",
              "      <td>12.020000</td>\n",
              "      <td>50.410000</td>\n",
              "      <td>185.200000</td>\n",
              "      <td>0.071170</td>\n",
              "      <td>0.027290</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.156500</td>\n",
              "      <td>0.055040</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>11.700000</td>\n",
              "      <td>16.170000</td>\n",
              "      <td>75.170000</td>\n",
              "      <td>420.300000</td>\n",
              "      <td>0.086370</td>\n",
              "      <td>0.064920</td>\n",
              "      <td>0.029560</td>\n",
              "      <td>0.020310</td>\n",
              "      <td>0.161900</td>\n",
              "      <td>0.057700</td>\n",
              "      <td>...</td>\n",
              "      <td>13.010000</td>\n",
              "      <td>21.080000</td>\n",
              "      <td>84.110000</td>\n",
              "      <td>515.300000</td>\n",
              "      <td>0.116600</td>\n",
              "      <td>0.147200</td>\n",
              "      <td>0.114500</td>\n",
              "      <td>0.064930</td>\n",
              "      <td>0.250400</td>\n",
              "      <td>0.071460</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>13.370000</td>\n",
              "      <td>18.840000</td>\n",
              "      <td>86.240000</td>\n",
              "      <td>551.100000</td>\n",
              "      <td>0.095870</td>\n",
              "      <td>0.092630</td>\n",
              "      <td>0.061540</td>\n",
              "      <td>0.033500</td>\n",
              "      <td>0.179200</td>\n",
              "      <td>0.061540</td>\n",
              "      <td>...</td>\n",
              "      <td>14.970000</td>\n",
              "      <td>25.410000</td>\n",
              "      <td>97.660000</td>\n",
              "      <td>686.500000</td>\n",
              "      <td>0.131300</td>\n",
              "      <td>0.211900</td>\n",
              "      <td>0.226700</td>\n",
              "      <td>0.099930</td>\n",
              "      <td>0.282200</td>\n",
              "      <td>0.080040</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>15.780000</td>\n",
              "      <td>21.800000</td>\n",
              "      <td>104.100000</td>\n",
              "      <td>782.700000</td>\n",
              "      <td>0.105300</td>\n",
              "      <td>0.130400</td>\n",
              "      <td>0.130700</td>\n",
              "      <td>0.074000</td>\n",
              "      <td>0.195700</td>\n",
              "      <td>0.066120</td>\n",
              "      <td>...</td>\n",
              "      <td>18.790000</td>\n",
              "      <td>29.720000</td>\n",
              "      <td>125.400000</td>\n",
              "      <td>1084.000000</td>\n",
              "      <td>0.146000</td>\n",
              "      <td>0.339100</td>\n",
              "      <td>0.382900</td>\n",
              "      <td>0.161400</td>\n",
              "      <td>0.317900</td>\n",
              "      <td>0.092080</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>28.110000</td>\n",
              "      <td>39.280000</td>\n",
              "      <td>188.500000</td>\n",
              "      <td>2501.000000</td>\n",
              "      <td>0.163400</td>\n",
              "      <td>0.345400</td>\n",
              "      <td>0.426800</td>\n",
              "      <td>0.201200</td>\n",
              "      <td>0.304000</td>\n",
              "      <td>0.097440</td>\n",
              "      <td>...</td>\n",
              "      <td>36.040000</td>\n",
              "      <td>49.540000</td>\n",
              "      <td>251.200000</td>\n",
              "      <td>4254.000000</td>\n",
              "      <td>0.222600</td>\n",
              "      <td>1.058000</td>\n",
              "      <td>1.252000</td>\n",
              "      <td>0.291000</td>\n",
              "      <td>0.663800</td>\n",
              "      <td>0.207500</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>8 rows × 30 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-18ef018c-3eff-4e50-b5b0-c8ad7db8b6c9')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-18ef018c-3eff-4e50-b5b0-c8ad7db8b6c9 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-18ef018c-3eff-4e50-b5b0-c8ad7db8b6c9');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tabel 2. Rata-rata dari variabel data\n",
        "Pada gambar di atas menunjukkan hasil dari hitungan rata-rata variabel data"
      ],
      "metadata": {
        "id": "vzuFog7VJVQ8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Visualisasi Data"
      ],
      "metadata": {
        "id": "RmjjN3uOBoTk"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Membagi dataset menjadi dua bagian yaitu categorial dan numerik"
      ],
      "metadata": {
        "id": "5UeA_Wf4EVeT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "categorical_features = ['diagnosis']\n",
        "numerical_features = [\n",
        "                      'radius_mean', \n",
        "                      'texture_mean', \n",
        "                      'perimeter_mean', \n",
        "                      'area_mean',\n",
        "                      'smoothness_mean',\n",
        "                      'compactness_mean',\n",
        "                      'concavity_mean',\n",
        "                      'concave points_mean',\n",
        "                      'symmetry_mean', \n",
        "                      'fractal_dimension_mean',\n",
        "                      'radius_se',\n",
        "                      'texture_se',\n",
        "                      'perimeter_se',\n",
        "                      'area_se', \n",
        "                      'smoothness_se',\n",
        "                      'compactness_se',\n",
        "                      'concavity_se',\n",
        "                      'concave points_se',\n",
        "                      'symmetry_se', \n",
        "                      'fractal_dimension_se',\n",
        "                      'radius_worst', \n",
        "                      'texture_worst',\n",
        "                      'perimeter_worst',\n",
        "                      'area_worst',\n",
        "                      'smoothness_worst',\n",
        "                      'compactness_worst', \n",
        "                      'concavity_worst',\n",
        "                      'concave points_worst',\n",
        "                      'symmetry_worst',\n",
        "                      'fractal_dimension_worst'\n",
        "                      ]"
      ],
      "metadata": {
        "id": "r3m6yDcPBrxb"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Distribusi kolom categorial"
      ],
      "metadata": {
        "id": "S22jiqmbB_zz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "feature = categorical_features[0]\n",
        "count = dt[feature].value_counts()\n",
        "percent = 100*dt[feature].value_counts(normalize=True)\n",
        "data = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})\n",
        "print(data)\n",
        "count.plot(kind='bar', title=feature);"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 335
        },
        "id": "_xZ-rQjzCGfW",
        "outputId": "f45c00de-075d-4409-c708-0a8dcfeaf2ec"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   jumlah sampel  persentase\n",
            "B            357        62.7\n",
            "M            212        37.3\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Gambar 1. Distribusi kolom kategorial \n",
        "Pada gambar di atas menunjukkan diagnosis kanker jinak lebih mendominasi."
      ],
      "metadata": {
        "id": "apMWCvsOHoXA"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Distribusi kolom numerik"
      ],
      "metadata": {
        "id": "6cEkXo9HCKX7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "dt.hist(bins=50, figsize=(20,15))\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 832
        },
        "id": "TZbBHIrhCRhL",
        "outputId": "1bf0dbc8-8ae1-472b-ba04-73a40459fa86"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1440x1080 with 30 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Korelasi setiap kolom"
      ],
      "metadata": {
        "id": "mF5yO7wxCke3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 8))\n",
        "correlation_matrix = dt.corr().round(2)\n",
        "\n",
        "sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )\n",
        "plt.title(\"Correlation Matrix untuk Fitur Numerik \", size=20)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 634
        },
        "id": "SWofFQ3yCnic",
        "outputId": "e35042e6-c268-4d99-de42-eb5e2f868d7c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'Correlation Matrix untuk Fitur Numerik ')"
            ]
          },
          "metadata": {},
          "execution_count": 18
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x576 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Persiapan Data atau Data Preparation"
      ],
      "metadata": {
        "id": "ioTKLXgkC2B6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Pengecekan pada kolom diagnosis yang bertipe objek \n",
        "\n",
        "**B** ditandai sebagai kanker jinak dan **M** ditandai kanker ganas"
      ],
      "metadata": {
        "id": "Kx66VHXpDZCC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Unique Values for Diagnosis\", dt['diagnosis'].unique())"
      ],
      "metadata": {
        "id": "PNDeixVKCv-t",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "69f86cde-4ab1-4393-c352-d915d283f7fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Unique Values for Diagnosis ['M' 'B']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "oh = OneHotEncoder()"
      ],
      "metadata": {
        "id": "nArZ48sLEcdt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Mapping pada kolom diagnosis dari type objek ke numerik agar bisa dibaca mesin"
      ],
      "metadata": {
        "id": "9fgkDmPDEhuf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "diagnosis_mapping = {'B': 0, 'M': 1}\n",
        "dt['diagnosis'] = dt['diagnosis'].map(diagnosis_mapping)\n",
        "\n",
        "dt"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 505
        },
        "id": "YCx3KzgsErpk",
        "outputId": "2228e525-c131-4114-fb19-f6721039a7be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     diagnosis  radius_mean  texture_mean  perimeter_mean  area_mean  \\\n",
              "0            1        17.99         10.38          122.80     1001.0   \n",
              "1            1        20.57         17.77          132.90     1326.0   \n",
              "2            1        19.69         21.25          130.00     1203.0   \n",
              "3            1        11.42         20.38           77.58      386.1   \n",
              "4            1        20.29         14.34          135.10     1297.0   \n",
              "..         ...          ...           ...             ...        ...   \n",
              "564          1        21.56         22.39          142.00     1479.0   \n",
              "565          1        20.13         28.25          131.20     1261.0   \n",
              "566          1        16.60         28.08          108.30      858.1   \n",
              "567          1        20.60         29.33          140.10     1265.0   \n",
              "568          0         7.76         24.54           47.92      181.0   \n",
              "\n",
              "     smoothness_mean  compactness_mean  concavity_mean  concave points_mean  \\\n",
              "0            0.11840           0.27760         0.30010              0.14710   \n",
              "1            0.08474           0.07864         0.08690              0.07017   \n",
              "2            0.10960           0.15990         0.19740              0.12790   \n",
              "3            0.14250           0.28390         0.24140              0.10520   \n",
              "4            0.10030           0.13280         0.19800              0.10430   \n",
              "..               ...               ...             ...                  ...   \n",
              "564          0.11100           0.11590         0.24390              0.13890   \n",
              "565          0.09780           0.10340         0.14400              0.09791   \n",
              "566          0.08455           0.10230         0.09251              0.05302   \n",
              "567          0.11780           0.27700         0.35140              0.15200   \n",
              "568          0.05263           0.04362         0.00000              0.00000   \n",
              "\n",
              "     symmetry_mean  ...  radius_worst  texture_worst  perimeter_worst  \\\n",
              "0           0.2419  ...        25.380          17.33           184.60   \n",
              "1           0.1812  ...        24.990          23.41           158.80   \n",
              "2           0.2069  ...        23.570          25.53           152.50   \n",
              "3           0.2597  ...        14.910          26.50            98.87   \n",
              "4           0.1809  ...        22.540          16.67           152.20   \n",
              "..             ...  ...           ...            ...              ...   \n",
              "564         0.1726  ...        25.450          26.40           166.10   \n",
              "565         0.1752  ...        23.690          38.25           155.00   \n",
              "566         0.1590  ...        18.980          34.12           126.70   \n",
              "567         0.2397  ...        25.740          39.42           184.60   \n",
              "568         0.1587  ...         9.456          30.37            59.16   \n",
              "\n",
              "     area_worst  smoothness_worst  compactness_worst  concavity_worst  \\\n",
              "0        2019.0           0.16220            0.66560           0.7119   \n",
              "1        1956.0           0.12380            0.18660           0.2416   \n",
              "2        1709.0           0.14440            0.42450           0.4504   \n",
              "3         567.7           0.20980            0.86630           0.6869   \n",
              "4        1575.0           0.13740            0.20500           0.4000   \n",
              "..          ...               ...                ...              ...   \n",
              "564      2027.0           0.14100            0.21130           0.4107   \n",
              "565      1731.0           0.11660            0.19220           0.3215   \n",
              "566      1124.0           0.11390            0.30940           0.3403   \n",
              "567      1821.0           0.16500            0.86810           0.9387   \n",
              "568       268.6           0.08996            0.06444           0.0000   \n",
              "\n",
              "     concave points_worst  symmetry_worst  fractal_dimension_worst  \n",
              "0                  0.2654          0.4601                  0.11890  \n",
              "1                  0.1860          0.2750                  0.08902  \n",
              "2                  0.2430          0.3613                  0.08758  \n",
              "3                  0.2575          0.6638                  0.17300  \n",
              "4                  0.1625          0.2364                  0.07678  \n",
              "..                    ...             ...                      ...  \n",
              "564                0.2216          0.2060                  0.07115  \n",
              "565                0.1628          0.2572                  0.06637  \n",
              "566                0.1418          0.2218                  0.07820  \n",
              "567                0.2650          0.4087                  0.12400  \n",
              "568                0.0000          0.2871                  0.07039  \n",
              "\n",
              "[569 rows x 31 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-af7422ff-2dd1-4ef7-8c72-3bc9b3842c3b\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>diagnosis</th>\n",
              "      <th>radius_mean</th>\n",
              "      <th>texture_mean</th>\n",
              "      <th>perimeter_mean</th>\n",
              "      <th>area_mean</th>\n",
              "      <th>smoothness_mean</th>\n",
              "      <th>compactness_mean</th>\n",
              "      <th>concavity_mean</th>\n",
              "      <th>concave points_mean</th>\n",
              "      <th>symmetry_mean</th>\n",
              "      <th>...</th>\n",
              "      <th>radius_worst</th>\n",
              "      <th>texture_worst</th>\n",
              "      <th>perimeter_worst</th>\n",
              "      <th>area_worst</th>\n",
              "      <th>smoothness_worst</th>\n",
              "      <th>compactness_worst</th>\n",
              "      <th>concavity_worst</th>\n",
              "      <th>concave points_worst</th>\n",
              "      <th>symmetry_worst</th>\n",
              "      <th>fractal_dimension_worst</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>17.99</td>\n",
              "      <td>10.38</td>\n",
              "      <td>122.80</td>\n",
              "      <td>1001.0</td>\n",
              "      <td>0.11840</td>\n",
              "      <td>0.27760</td>\n",
              "      <td>0.30010</td>\n",
              "      <td>0.14710</td>\n",
              "      <td>0.2419</td>\n",
              "      <td>...</td>\n",
              "      <td>25.380</td>\n",
              "      <td>17.33</td>\n",
              "      <td>184.60</td>\n",
              "      <td>2019.0</td>\n",
              "      <td>0.16220</td>\n",
              "      <td>0.66560</td>\n",
              "      <td>0.7119</td>\n",
              "      <td>0.2654</td>\n",
              "      <td>0.4601</td>\n",
              "      <td>0.11890</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>20.57</td>\n",
              "      <td>17.77</td>\n",
              "      <td>132.90</td>\n",
              "      <td>1326.0</td>\n",
              "      <td>0.08474</td>\n",
              "      <td>0.07864</td>\n",
              "      <td>0.08690</td>\n",
              "      <td>0.07017</td>\n",
              "      <td>0.1812</td>\n",
              "      <td>...</td>\n",
              "      <td>24.990</td>\n",
              "      <td>23.41</td>\n",
              "      <td>158.80</td>\n",
              "      <td>1956.0</td>\n",
              "      <td>0.12380</td>\n",
              "      <td>0.18660</td>\n",
              "      <td>0.2416</td>\n",
              "      <td>0.1860</td>\n",
              "      <td>0.2750</td>\n",
              "      <td>0.08902</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>19.69</td>\n",
              "      <td>21.25</td>\n",
              "      <td>130.00</td>\n",
              "      <td>1203.0</td>\n",
              "      <td>0.10960</td>\n",
              "      <td>0.15990</td>\n",
              "      <td>0.19740</td>\n",
              "      <td>0.12790</td>\n",
              "      <td>0.2069</td>\n",
              "      <td>...</td>\n",
              "      <td>23.570</td>\n",
              "      <td>25.53</td>\n",
              "      <td>152.50</td>\n",
              "      <td>1709.0</td>\n",
              "      <td>0.14440</td>\n",
              "      <td>0.42450</td>\n",
              "      <td>0.4504</td>\n",
              "      <td>0.2430</td>\n",
              "      <td>0.3613</td>\n",
              "      <td>0.08758</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>11.42</td>\n",
              "      <td>20.38</td>\n",
              "      <td>77.58</td>\n",
              "      <td>386.1</td>\n",
              "      <td>0.14250</td>\n",
              "      <td>0.28390</td>\n",
              "      <td>0.24140</td>\n",
              "      <td>0.10520</td>\n",
              "      <td>0.2597</td>\n",
              "      <td>...</td>\n",
              "      <td>14.910</td>\n",
              "      <td>26.50</td>\n",
              "      <td>98.87</td>\n",
              "      <td>567.7</td>\n",
              "      <td>0.20980</td>\n",
              "      <td>0.86630</td>\n",
              "      <td>0.6869</td>\n",
              "      <td>0.2575</td>\n",
              "      <td>0.6638</td>\n",
              "      <td>0.17300</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>20.29</td>\n",
              "      <td>14.34</td>\n",
              "      <td>135.10</td>\n",
              "      <td>1297.0</td>\n",
              "      <td>0.10030</td>\n",
              "      <td>0.13280</td>\n",
              "      <td>0.19800</td>\n",
              "      <td>0.10430</td>\n",
              "      <td>0.1809</td>\n",
              "      <td>...</td>\n",
              "      <td>22.540</td>\n",
              "      <td>16.67</td>\n",
              "      <td>152.20</td>\n",
              "      <td>1575.0</td>\n",
              "      <td>0.13740</td>\n",
              "      <td>0.20500</td>\n",
              "      <td>0.4000</td>\n",
              "      <td>0.1625</td>\n",
              "      <td>0.2364</td>\n",
              "      <td>0.07678</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>564</th>\n",
              "      <td>1</td>\n",
              "      <td>21.56</td>\n",
              "      <td>22.39</td>\n",
              "      <td>142.00</td>\n",
              "      <td>1479.0</td>\n",
              "      <td>0.11100</td>\n",
              "      <td>0.11590</td>\n",
              "      <td>0.24390</td>\n",
              "      <td>0.13890</td>\n",
              "      <td>0.1726</td>\n",
              "      <td>...</td>\n",
              "      <td>25.450</td>\n",
              "      <td>26.40</td>\n",
              "      <td>166.10</td>\n",
              "      <td>2027.0</td>\n",
              "      <td>0.14100</td>\n",
              "      <td>0.21130</td>\n",
              "      <td>0.4107</td>\n",
              "      <td>0.2216</td>\n",
              "      <td>0.2060</td>\n",
              "      <td>0.07115</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>565</th>\n",
              "      <td>1</td>\n",
              "      <td>20.13</td>\n",
              "      <td>28.25</td>\n",
              "      <td>131.20</td>\n",
              "      <td>1261.0</td>\n",
              "      <td>0.09780</td>\n",
              "      <td>0.10340</td>\n",
              "      <td>0.14400</td>\n",
              "      <td>0.09791</td>\n",
              "      <td>0.1752</td>\n",
              "      <td>...</td>\n",
              "      <td>23.690</td>\n",
              "      <td>38.25</td>\n",
              "      <td>155.00</td>\n",
              "      <td>1731.0</td>\n",
              "      <td>0.11660</td>\n",
              "      <td>0.19220</td>\n",
              "      <td>0.3215</td>\n",
              "      <td>0.1628</td>\n",
              "      <td>0.2572</td>\n",
              "      <td>0.06637</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>566</th>\n",
              "      <td>1</td>\n",
              "      <td>16.60</td>\n",
              "      <td>28.08</td>\n",
              "      <td>108.30</td>\n",
              "      <td>858.1</td>\n",
              "      <td>0.08455</td>\n",
              "      <td>0.10230</td>\n",
              "      <td>0.09251</td>\n",
              "      <td>0.05302</td>\n",
              "      <td>0.1590</td>\n",
              "      <td>...</td>\n",
              "      <td>18.980</td>\n",
              "      <td>34.12</td>\n",
              "      <td>126.70</td>\n",
              "      <td>1124.0</td>\n",
              "      <td>0.11390</td>\n",
              "      <td>0.30940</td>\n",
              "      <td>0.3403</td>\n",
              "      <td>0.1418</td>\n",
              "      <td>0.2218</td>\n",
              "      <td>0.07820</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>567</th>\n",
              "      <td>1</td>\n",
              "      <td>20.60</td>\n",
              "      <td>29.33</td>\n",
              "      <td>140.10</td>\n",
              "      <td>1265.0</td>\n",
              "      <td>0.11780</td>\n",
              "      <td>0.27700</td>\n",
              "      <td>0.35140</td>\n",
              "      <td>0.15200</td>\n",
              "      <td>0.2397</td>\n",
              "      <td>...</td>\n",
              "      <td>25.740</td>\n",
              "      <td>39.42</td>\n",
              "      <td>184.60</td>\n",
              "      <td>1821.0</td>\n",
              "      <td>0.16500</td>\n",
              "      <td>0.86810</td>\n",
              "      <td>0.9387</td>\n",
              "      <td>0.2650</td>\n",
              "      <td>0.4087</td>\n",
              "      <td>0.12400</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>568</th>\n",
              "      <td>0</td>\n",
              "      <td>7.76</td>\n",
              "      <td>24.54</td>\n",
              "      <td>47.92</td>\n",
              "      <td>181.0</td>\n",
              "      <td>0.05263</td>\n",
              "      <td>0.04362</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.1587</td>\n",
              "      <td>...</td>\n",
              "      <td>9.456</td>\n",
              "      <td>30.37</td>\n",
              "      <td>59.16</td>\n",
              "      <td>268.6</td>\n",
              "      <td>0.08996</td>\n",
              "      <td>0.06444</td>\n",
              "      <td>0.0000</td>\n",
              "      <td>0.0000</td>\n",
              "      <td>0.2871</td>\n",
              "      <td>0.07039</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>569 rows × 31 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-af7422ff-2dd1-4ef7-8c72-3bc9b3842c3b')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-af7422ff-2dd1-4ef7-8c72-3bc9b3842c3b button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-af7422ff-2dd1-4ef7-8c72-3bc9b3842c3b');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tabel 3. Mapping pada kolom diagnosis\n",
        "Pada gambar di atas menunjukkan hasil mapping pada kolom diagnosis dari type objek ke numerik agar bisa dibaca mesin."
      ],
      "metadata": {
        "id": "a-x__CCzJmMF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Menghitung jumlah baris pada kolom target"
      ],
      "metadata": {
        "id": "Btd1R0-jEztW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dt.diagnosis.value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "blTHr5Z5E6aU",
        "outputId": "65cd8b10-f5d1-4462-a002-d7885ef4a4bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    357\n",
              "1    212\n",
              "Name: diagnosis, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Pembagian Dataset dengan train_test_split "
      ],
      "metadata": {
        "id": "_f2nPIIHFDar"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X = dt.drop('diagnosis',axis=1)\n",
        "y = dt['diagnosis']"
      ],
      "metadata": {
        "id": "b6_4Kz7yFACD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)"
      ],
      "metadata": {
        "id": "wcsEFUlUHjFq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Menghitung banyaknya data latih dan data test"
      ],
      "metadata": {
        "id": "ntz0vmO_HrpY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(f'Total # of sample in whole dataset: {len(X)}')\n",
        "print(f'Total # of sample in train dataset: {len(X_train)}')\n",
        "print(f'Total # of sample in test dataset: {len(X_test)}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gIWR5bivHjQh",
        "outputId": "64e7ada3-4eb9-4194-df1c-24ab4e78d251"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total # of sample in whole dataset: 569\n",
            "Total # of sample in train dataset: 455\n",
            "Total # of sample in test dataset: 114\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Melakukan Standart Scaller"
      ],
      "metadata": {
        "id": "G4AxJ09WH17v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sc=StandardScaler()\n",
        "\n",
        "X_train = sc.fit_transform(X_train)\n",
        "X_test = sc.transform(X_test)"
      ],
      "metadata": {
        "id": "0UurMeaQH0B2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Pembuatan Model atau Model Development"
      ],
      "metadata": {
        "id": "-BQQkC5OIFCx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Menyiapkan dataframe sebagai analisis model"
      ],
      "metadata": {
        "id": "ItlxT3vrLFOz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "models = pd.DataFrame(index=['train_mse', 'test_mse'], \n",
        "                      columns=['RandomForest', 'KNN', 'Boosting'])"
      ],
      "metadata": {
        "id": "UNGhs7tHIJh1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Algoritma Random Forest"
      ],
      "metadata": {
        "id": "EPoE5jltKExl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "RFC = RandomForestClassifier()\n",
        "RFC.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QG9bb8QUJ5vj",
        "outputId": "7099c9bf-951a-42dc-8f13-8312ed2c3b88"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestClassifier()"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Menguji model pada data test yang dijalankan"
      ],
      "metadata": {
        "id": "Oag_1EXpKKgh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "RFC_pred = RFC.predict(X_test)"
      ],
      "metadata": {
        "id": "cIQyICSPKSee"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "AKURASI SKOR"
      ],
      "metadata": {
        "id": "QEOH-vKaKEak"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "accuracy_score(y_test, RFC_pred)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MDq-cIKhKejs",
        "outputId": "a14d2e67-8ad7-4865-c67c-0a8a67b731eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9736842105263158"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Klasifikasi report"
      ],
      "metadata": {
        "id": "G75Uef86KCD9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "RFC_cr = classification_report(y_test, RFC_pred, output_dict=True)\n",
        "pd.DataFrame(RFC_cr).transpose()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "1rJV3DLZKjq3",
        "outputId": "518a2547-7eb9-4b29-ba10-902a60fca8a9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              precision    recall  f1-score     support\n",
              "0              0.956522  1.000000  0.977778   66.000000\n",
              "1              1.000000  0.937500  0.967742   48.000000\n",
              "accuracy       0.973684  0.973684  0.973684    0.973684\n",
              "macro avg      0.978261  0.968750  0.972760  114.000000\n",
              "weighted avg   0.974828  0.973684  0.973552  114.000000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e2f82cd1-1159-4677-b5e6-abf36c939345\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>precision</th>\n",
              "      <th>recall</th>\n",
              "      <th>f1-score</th>\n",
              "      <th>support</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.956522</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.977778</td>\n",
              "      <td>66.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.937500</td>\n",
              "      <td>0.967742</td>\n",
              "      <td>48.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>accuracy</th>\n",
              "      <td>0.973684</td>\n",
              "      <td>0.973684</td>\n",
              "      <td>0.973684</td>\n",
              "      <td>0.973684</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>macro avg</th>\n",
              "      <td>0.978261</td>\n",
              "      <td>0.968750</td>\n",
              "      <td>0.972760</td>\n",
              "      <td>114.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>weighted avg</th>\n",
              "      <td>0.974828</td>\n",
              "      <td>0.973684</td>\n",
              "      <td>0.973552</td>\n",
              "      <td>114.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e2f82cd1-1159-4677-b5e6-abf36c939345')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e2f82cd1-1159-4677-b5e6-abf36c939345 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e2f82cd1-1159-4677-b5e6-abf36c939345');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tabel 4. Klasifikasi report \n",
        "Pada tabel di atas menunjukkan hasil berbentuk tabel klasifikasi report pada dataset."
      ],
      "metadata": {
        "id": "sMtAgi6BJ2eg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Algoritma K-Nearesst Neighbor"
      ],
      "metadata": {
        "id": "fJFMZXkXLzEn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "KNNT = KNeighborsClassifier()\n",
        "KNNT.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LsSGbE10L702",
        "outputId": "80d78535-2216-47f2-98fc-9229b87b0d96"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "KNeighborsClassifier()"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Menguji model pada data test"
      ],
      "metadata": {
        "id": "-mCbhxeOLJVJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "KNNT_pred = KNNT.predict(X_test)"
      ],
      "metadata": {
        "id": "PND2HJujMSFl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "accuracy_score(y_test, KNNT_pred)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8ZRUo2V6MZB3",
        "outputId": "19db2101-6a6d-4ca4-e9df-a12b9cc5d2d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9649122807017544"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "KNNT_cr = classification_report(y_test, KNNT_pred, output_dict=True)\n",
        "pd.DataFrame(KNNT_cr).transpose()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "MSqJKipeN1Uj",
        "outputId": "b7cf6918-b7c8-47cf-a44c-8fe112306168"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              precision    recall  f1-score     support\n",
              "0              0.942857  1.000000  0.970588   66.000000\n",
              "1              1.000000  0.916667  0.956522   48.000000\n",
              "accuracy       0.964912  0.964912  0.964912    0.964912\n",
              "macro avg      0.971429  0.958333  0.963555  114.000000\n",
              "weighted avg   0.966917  0.964912  0.964666  114.000000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3f2c12a6-71bf-4146-b624-40e9e528496a\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>precision</th>\n",
              "      <th>recall</th>\n",
              "      <th>f1-score</th>\n",
              "      <th>support</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.942857</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.970588</td>\n",
              "      <td>66.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.916667</td>\n",
              "      <td>0.956522</td>\n",
              "      <td>48.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>accuracy</th>\n",
              "      <td>0.964912</td>\n",
              "      <td>0.964912</td>\n",
              "      <td>0.964912</td>\n",
              "      <td>0.964912</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>macro avg</th>\n",
              "      <td>0.971429</td>\n",
              "      <td>0.958333</td>\n",
              "      <td>0.963555</td>\n",
              "      <td>114.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>weighted avg</th>\n",
              "      <td>0.966917</td>\n",
              "      <td>0.964912</td>\n",
              "      <td>0.964666</td>\n",
              "      <td>114.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3f2c12a6-71bf-4146-b624-40e9e528496a')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3f2c12a6-71bf-4146-b624-40e9e528496a button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3f2c12a6-71bf-4146-b624-40e9e528496a');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tabel 5. Klasifikasi report dengan algoritma k-nearest neighbor\n"
      ],
      "metadata": {
        "id": "d7XVGFYXKaHR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Evaluasi Model"
      ],
      "metadata": {
        "id": "ctK1Q0CFN7L4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Perbandingan Metriks Antar Model"
      ],
      "metadata": {
        "id": "F7ucx7R1ODIL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "RFC_cr['accuracy']"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "82EjiwroOCIG",
        "outputId": "f1e320e1-1fcf-4118-97f0-9abd6f84918e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9736842105263158"
            ]
          },
          "metadata": {},
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Mengolah hasil laporan klasifikasi model pada data frame"
      ],
      "metadata": {
        "id": "4SRCGSmlLOp-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "metrics = pd.DataFrame({'accuracy' : [RFC_cr['accuracy'], KNNT_cr['accuracy']],\n",
        "                        'f1-score_0' : [RFC_cr['0']['f1-score'],KNNT_cr['0']['f1-score']],\n",
        "                        'precision_0' : [RFC_cr['0']['precision'],KNNT_cr['0']['precision']],\n",
        "                        'recall_0' : [RFC_cr['0']['recall'],KNNT_cr['0']['recall']],\n",
        "                        'f1-score_1' : [RFC_cr['1']['f1-score'],KNNT_cr['1']['f1-score']],\n",
        "                        'precision_1' : [RFC_cr['1']['precision'],KNNT_cr['1']['precision']],\n",
        "                        'recall_1' : [RFC_cr['1']['recall'],KNNT_cr['1']['recall']]},\n",
        "                        index=['RFC','KNNT'])\n",
        "multiheader = [('','accuracy'),\n",
        "               ('0', 'f1-score'),\n",
        "               ('0', 'precision'),\n",
        "               ('0', 'recall'),\n",
        "               ('1', 'f1-score'),\n",
        "               ('1', 'precision'),\n",
        "               ('1', 'recall')]\n",
        "metrics.columns = pd.MultiIndex.from_tuples(multiheader)\n",
        "# Menampilkan model dataframe\n",
        "metrics"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "UX7JerytN-kK",
        "outputId": "15a4641b-eacd-48b5-b712-cc325d7439d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                       0                          1                    \n",
              "      accuracy  f1-score precision recall  f1-score precision    recall\n",
              "RFC   0.973684  0.977778  0.956522    1.0  0.967742       1.0  0.937500\n",
              "KNNT  0.964912  0.970588  0.942857    1.0  0.956522       1.0  0.916667"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-55d4d405-67d7-4950-a65c-e01e10dd1046\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead tr th {\n",
              "        text-align: left;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th colspan=\"3\" halign=\"left\">0</th>\n",
              "      <th colspan=\"3\" halign=\"left\">1</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th>accuracy</th>\n",
              "      <th>f1-score</th>\n",
              "      <th>precision</th>\n",
              "      <th>recall</th>\n",
              "      <th>f1-score</th>\n",
              "      <th>precision</th>\n",
              "      <th>recall</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>RFC</th>\n",
              "      <td>0.973684</td>\n",
              "      <td>0.977778</td>\n",
              "      <td>0.956522</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.967742</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.937500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>KNNT</th>\n",
              "      <td>0.964912</td>\n",
              "      <td>0.970588</td>\n",
              "      <td>0.942857</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.956522</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.916667</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-55d4d405-67d7-4950-a65c-e01e10dd1046')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-55d4d405-67d7-4950-a65c-e01e10dd1046 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-55d4d405-67d7-4950-a65c-e01e10dd1046');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tabel 6. Akurasi dengan algoritma random forest dan k-nearest neighbor\n",
        "Pada gambar di atas menampilkan model dataframe dengan dua macam algoritma yang berbeda. "
      ],
      "metadata": {
        "id": "cM0oqek1KsNl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Confussion Matrixx"
      ],
      "metadata": {
        "id": "6-zn-cEQObG8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Visualisasi Algoritma Random Forest"
      ],
      "metadata": {
        "id": "X3UQMYwBO8rL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Algoritma Random Forest"
      ],
      "metadata": {
        "id": "hw0SE8a3LTyD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "RFC_cm = confusion_matrix(y_test,RFC_pred)\n",
        "sns.heatmap(RFC_cm,annot=True,fmt=\"d\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 283
        },
        "id": "mDvKUmtpO6of",
        "outputId": "e37e3e2b-0a1e-47b4-89fa-3ba2591cdee4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f1bfc822190>"
            ]
          },
          "metadata": {},
          "execution_count": 42
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Gambar 2. Visualisasi algoritma random forest \n",
        "Pada gambar di atas menunjukkan  menjelaskan bahwa bagian atas kiri merepresentasikan TN (True negatif) yaitu data negatif yg diprediksi benar, dan bagian bawah kanan merupakan data positif yg di prediksi benar, selain itu merupakan data false negatif (atas kanan) dan false positif (bawah kiri), dimana hasil itu merupakan data negatif namun diprediksi positif maupun sebaliknya."
      ],
      "metadata": {
        "id": "a9_gz6oaIPBj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Visualisasi Algoritma K-Nearest Neighbor"
      ],
      "metadata": {
        "id": "sV1YKI5OPRvG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Algoritma K-Nearest Neighbor"
      ],
      "metadata": {
        "id": "-nQKHVxDLZfl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "KNNT_cm = confusion_matrix(y_test,KNNT_pred)\n",
        "sns.heatmap(KNNT_cm,annot=True,fmt=\"d\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 283
        },
        "id": "K6zWaEOdPV3r",
        "outputId": "60136a64-6dc1-44c0-8133-6664427db0d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f1bfd1e3090>"
            ]
          },
          "metadata": {},
          "execution_count": 43
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Gambar 3. Algoritma K-Nearest Neighbor\n",
        "Pada gambar di atas menunjukkan bahwa tidak jauh berbeda dengan algoritma random forest dimana bagian atas kiri merepresentasikan TN (True Negatif) yaitu data negatif yg diprediksi benar, dan bagian bawah kanan merupakan data positif yg di prediksi benar, selain itu merupakan data false negatif (atas kanan) dan false positif (bawah kiri), dimana hasil itu merupakan data negatif namun diprediksi positif maupun sebaliknya."
      ],
      "metadata": {
        "id": "Muw7eyMnIq55"
      }
    }
  ]
}