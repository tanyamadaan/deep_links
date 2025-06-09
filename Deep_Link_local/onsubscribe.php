<?php
namespace Custom\Common\Controller\Ondc;

use Magento\Framework\App\Action\Action;
use Magento\Framework\App\Action\Context;
use Magento\Framework\Controller\Result\JsonFactory;
use Psr\Log\LoggerInterface;

// class OnSubscribe extends Action
// {
    
	/**
     * Execute the controller action.
     */
    public function execute()
    {
        $request = $this->getRequest();
        $postData = $request->getPostValue();
        $request->setMethod('POST');

        $pubDirectory = $this->_objectManager->get('Magento\Framework\App\Filesystem\DirectoryList')->getPath('pub');
        $logFilePath = $pubDirectory . '/media/';

        $requestJsonData = file_get_contents('php://input');
        $requestData = json_decode($requestJsonData, true);
        $writeLogFileReq = file_put_contents($logFilePath . 'on_subscribe_req.txt', $requestJsonData);

        $response = [
            "ack" => [
                "status" => "ACK"
            ]
        ];
        print_r(json_encode($response));

        exit;
    }

    
    function decryptAES256ECB($key, $encrypted) {

        $pubDirectory = $this->_objectManager->get('Magento\Framework\App\Filesystem\DirectoryList')->getPath('pub');
        $logFilePath = $pubDirectory . '/media/';
        // ECB doesn't use IV
        $iv = '';
    
        // Create a cipher object
        $decipher = openssl_decrypt($encrypted, 'aes-256-ecb', $key, OPENSSL_RAW_DATA | OPENSSL_ZERO_PADDING, $iv);
    
        if ($decipher === false) {
            echo "Decryption failed: " . openssl_error_string() . "\n";
            return false;
        }
    
        // Remove the PKCS#7 padding manually
        $padding = ord($decipher[strlen($decipher) - 1]);

        $requestData2 = json_encode($decipher, true);
        $writeLogFileReq2 = file_put_contents($logFilePath . 'on_subscribe_decipher.txt', $requestData2);
    
        // Check if padding is valid
        if ($padding > 0 && $padding <= 16) {
            $decipher = substr($decipher, 0, strlen($decipher) - $padding);
            //$response = ["answer" => $decipher];
            return $decipher;
        } else {
            // Handle invalid padding
            return false;
        }
    }


    /**
     * Action for handling on_subscribe.
     *
     * @return \Magento\Framework\Controller\ResultInterface
     */
    public function on_subscribeAction()
    {
        $request = $this->getRequest();
        $postData = $request->getPostValue();
        $request->setMethod('POST');

        $pubDirectory = $this->_objectManager->get('Magento\Framework\App\Filesystem\DirectoryList')->getPath('pub');
        $logFilePath = $pubDirectory . '/media/';

        $requestJsonData = file_get_contents('php://input');
        $requestData = json_decode($requestJsonData, true);
        $writeLogFileReq = file_put_contents($logFilePath . 'on_subscribe_req1.txt', $requestJsonData);
        
        /*** test code */

        /** test code */

        $challenge = $requestData['challenge'];
        
        $privateKey = "MC4CAQAwBQYDK2VuBCIEIHiEMgBIVh37wH1foXGSfCnWHETyId7Si3f/d4GnWsF7";
        $publicKey_ondc = "MCowBQYDK2VuAyEAduMuZgmtpjdCuxv+Nc49K0cB6tL/Dj3HZetvVN7ZekM=";
        $privateKeyBinary = base64_decode($privateKey);
        $publicKeyBinary = base64_decode($publicKey_ondc);

        // Convert the private key to OpenSSLAsymmetricKey
        $privateKeyObject = openssl_pkey_get_private("-----BEGIN PRIVATE KEY-----\n" . chunk_split(base64_encode($privateKeyBinary), 64, "\n") . "-----END PRIVATE KEY-----");
        
        if ($privateKeyObject === false) {
            die('Error loading private key: ' . openssl_error_string());
        }

        if ($privateKeyObject === false) {
            echo "ERROR: ".openssl_error_string() . "\n";
            exit;
        }
        $encryptionKey = openssl_dh_compute_key($publicKeyBinary,$privateKeyObject);
        
        $answer = $this->decryptAES256ECB($encryptionKey, base64_decode($challenge));
        
        $response = ['answer' => $answer];
        // $response = ['answer' => 'dd557389-f7f4-47dd-ac34-f072fc91b4a7'];
        
        //$writeLogFileResp3 = file_put_contents($logFilePath . 'suscribe_Respponse.txt', $response);
        // Set the appropriate headers and status code
        header('Content-Type: application/json');
        http_response_code(200);

        // Send the JSON response
        echo json_encode($response);

        exit;

        // You should use ResultInterface to handle the response in a standardized way
        // $resultJson = $this->resultJsonFactory->create();
        // return $resultJson->setData($response);
		
		$response = [
			"ack" => [
				"status" => "ACK"
			]
		];
			
		
		print_r(json_encode($response));
        exit;
    }
}
