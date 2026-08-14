function geradorQRCode(){
   let texto=document.getElementById("texto").value;
   let qrcode=document.getElementById("qrcode");

   qrcode.innerHTML=""

   if(texto == ""){
        alert("Digete um texto ou link")
        return
   }
   new QRCode(qrcode,{
      text:texto,
      width:200,
      height:200
   })
}