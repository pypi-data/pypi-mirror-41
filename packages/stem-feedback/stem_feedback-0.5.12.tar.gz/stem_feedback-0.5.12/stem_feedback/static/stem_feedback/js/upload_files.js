$(function(){
    $("input[type='submit']").click(function(){
        let fileUpload = $("input[type='file']");
        if (parseInt(fileUpload.get(0).files.length)>5){
         alert("Вы можете добавить только 5 файлов");
        }
    });
});