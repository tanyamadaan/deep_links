const QRCode = require("qrcode");
const { createCanvas, loadImage } = require("canvas");
const fs = require('fs');

async function create(dataForQRcode, center_image, width, cwidth) {
  const canvas = createCanvas(width, width);
  QRCode.toCanvas(
    canvas,
    dataForQRcode,
    {
      errorCorrectionLevel: "H",
      margin: 2,
      scale: 20,
      color: {
        dark: "#000000",
        light: "#ffffff",
      },
    }
  );

  const ctx = canvas.getContext("2d");
  const img = await loadImage(center_image);
  const center = (width - cwidth) / 2;
  ctx.drawImage(img, center, center, cwidth, cwidth);
  return canvas.toDataURL("image/png");
}

async function main() {
  const qrCode = await create(
    "http://example.com",
    "logo.png",
    150,
    50
  );

const fileName = 'qr_code_test.png'
// Write the data URL to a file
fs.writeFileSync(fileName, qrCode.split(';base64,').pop(), { encoding: 'base64' });
console.log('QR code saved as qr_code.png');

  console.log(qrCode);
}

main()

// const fileName = 'qr_code_test.png'
// const qrCode = create(
//     "http://example.com",
//     "logo.png",
//     150,
//     50
//   );
// fs.writeFileSync(fileName, qrCode);
// console.log(qrCode);