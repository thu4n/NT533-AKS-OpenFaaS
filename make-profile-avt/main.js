const imageInput = document.getElementById("imageInput");
const uploadedImage = document.getElementById("uploadedImage");
const convertBtn = document.getElementById("convertBtn");
const downloadBtn = document.getElementById("downloadBtn");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let inputImg = null;

function loadImage(src) {
  let img = new Image();
  img.src = src;
  return img;
}

imageInput.addEventListener("change", function (e) {
  if (e.target.files && e.target.files[0]) {
    const reader = new FileReader();
    reader.readAsDataURL(e.target.files[0]);
    inputImg = loadImage(URL.createObjectURL(e.target.files[0]));
    uploadedImage.src = URL.createObjectURL(e.target.files[0]);
    uploadedImage.setAttribute("style", "display: block");
  }
});

convertBtn.addEventListener("click", function () {
  const response = postData(
    "https://faas.thu4n.dev/function/make-profile-avt",
    {
      data: inputImg.src,
    }
  )
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

async function postData(url, { data }) {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify(data),
    });
    return response.json();
  } catch (error) {
    console.error("Error:", error);
  }
}
