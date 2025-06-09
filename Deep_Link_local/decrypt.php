<?php

$crypto_private_key = "-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VuBCIEIPCiBwP28ZH8+xd+mXc2G28Jrf97cZO21vTKkP6mi5tS
-----END PRIVATE KEY-----";

$crypto_public_key = "-----BEGIN PUBLIC KEY-----
MCowBQYDK2VuAyEAdp/CNA3s5KdW6TRWZ7aLL0suRPwgehQKWCf8dqUBqgE=
-----END PUBLIC KEY-----";

function decrypt($crypto_private_key, $crypto_public_key, $cipherstring) {
    // Decode base64 and load private key
    $private_key = openssl_pkey_get_private($crypto_private_key);

    // Decode base64 and load public key
    $public_key = openssl_pkey_get_public($crypto_public_key);

    // // Extract public key details
    // $public_key_details = openssl_pkey_get_details($public_key);
    // $public_key_key = $public_key_details['key'];

    // $sharedKey = openssl_pkey_derive([
    //     'private_key' => $private_key,
    //     'public_key' => $public_key,
    // ], ['algorithm' => OPENSSL_ALGO_SHA256, 'passphrase' => '']);

    $sharedKey = openssl_pkey_derive($public_key, $private_key);
    echo $sharedKey;

    // Decode base64 and decrypt cipher string using AES
    $cipher = base64_decode($cipherstring);
    echo $cipher;

    //$decryptedChallenge = decryptAES256ECB($sharedKey, $cipher);
    $decrypted = openssl_decrypt($cipher, 'aes-256-ecb', $sharedKey, OPENSSL_RAW_DATA);


    echo 'testbjkkkklkl';
    echo $decrypted;
    // openssl_decrypt($cipher, 'aes-256-ecb', $shared_key, OPENSSL_RAW_DATA);
    // $decrypted = openssl_decrypt($cipher, 'aes-256-ecb', $shared_key, OPENSSL_RAW_DATA);
    // openssl_private_decrypt($public_key_key, $shared_key, $private_key);

    return unpad($decrypted);
    // Perform key exchange to get shared key
    // if (openssl_private_decrypt($public_key_key, $shared_key, $private_key)) {
    //     // Decode base64 and decrypt cipher string using AES
    //     $cipher = base64_decode($cipherstring);
    //     echo $cipher;
    //     openssl_decrypt($cipher, 'aes-256-ecb', $shared_key, OPENSSL_RAW_DATA);
    //     $decrypted = openssl_decrypt($cipher, 'aes-256-ecb', $shared_key, OPENSSL_RAW_DATA);
    // } else {
    //     return "Key exchange failed.";
    // }
}

function unpad($data) {
    $pad = ord($data[strlen($data) - 1]);
    return substr($data, 0, -$pad);
}

$cipherstring = "uIMyLZ5RpC9tNYu2mJgLBn0Z3JecWca5PSpLMCLcUaTVpsgY/yLWx2vpKSc0pE9FbdwQJMy+umvldNBk2r9WhWQ==";

$result = decrypt($crypto_private_key, $crypto_public_key, $cipherstring);

echo "Decrypted Result: " . $result . PHP_EOL;

?>
