const QRCode = require('qrcode');
const { createCanvas, loadImage } = require('canvas');
const fs = require('fs');

async function generateQRCode(deepLink, fileName = 'qr_code_new.png') {
    try {
        // Create QR code with deep link embedded
        // const qrCodeOptions = {
        //     errorCorrectionLevel: 'H',
        //     type: 'png',
        //     quality: 0.92,
        //     margin: 1,
        //     width: 400,
        // };

        const qrCodeOptions = {
            errorCorrectionLevel: 'M', // Adjust error correction level (M for medium)
            margin: 1, // Adjust margin
            width: 400, // Adjust width
            color: {
                dark: '#000000', // Adjust color
                light: '#ffffff' // Adjust color
            }
        };

        const qrCodeDataURL = await QRCode.toDataURL(deepLink, qrCodeOptions);

        const canvas = createCanvas(400, 400);
        const ctx = canvas.getContext('2d');

        // Draw QR code on canvas
        const img = await loadImage(qrCodeDataURL);
        ctx.drawImage(img, 0, 0, 400, 400);

        // Load the logo image
        const logo = await loadImage('logo.png'); // Path to your logo image

        // // Calculate the position to center the logo on the QR code
        // const logoPosition = {
        //     x: (canvas.width - logo.width) / 2,
        //     y: (canvas.height - logo.height) / 2,
        // };

        // // Paste the logo onto the QR code
        // ctx.drawImage(logo, logoPosition.x, logoPosition.y);

        // Resize the logo image
        const basewidth = 100; // Adjust the desired width of the logo
        const wpercent = basewidth / logo.width;
        const hsize = logo.height * wpercent;
        ctx.drawImage(logo, (canvas.width - basewidth) / 2, (canvas.height - hsize) / 2, basewidth, hsize);


        // Save the canvas as an image file
        const qrCodeImage = canvas.toBuffer();
        fs.writeFileSync(fileName, qrCodeImage);
        console.log(`QR code generated and saved as ${fileName}`);
    } catch (error) {
        console.error('Error generating QR code:', error);
    }
}

// Example usage
generateQRCode('https://example.com');