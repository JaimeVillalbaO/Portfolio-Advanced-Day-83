<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];

    // Configura los detalles del correo
    $to = "jaimevillalbaoyola@gmail.com";
    $headers = "From: $email";
    $body = "Nombre: $name\nCorreo electrónico: $email\nAsunto: $subject\nMensaje:\n$message";

    // Envía el correo
    if (mail($to, $subject, $body, $headers)) {
        echo "success";
    } else {
        echo "error";
    }
}
?>