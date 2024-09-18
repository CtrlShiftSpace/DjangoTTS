$(document).ready(function (){
    // 按下聆聽按鈕
    $("#btn-trans-audio").on('click', transAudioHandler);
});

function transAudioHandler(e) {
    let comm_text = $("#input-trans-audio").val();
    // 未輸入單字或句子
    if (comm_text.trim() == "") {
        return;
    }

    $.ajax({
        type: 'POST',
        url: "/api/edge/tts",
        data: {
            comm_text: comm_text
        },
        beforeSend: function( xhr ) {
            xhr.overrideMimeType( "text/plain;" );
        }
    })
    .done(function( data ) {
        if ( console && console.log ) {
            console.log(data);
            let json = JSON.parse(data);
            // 播放聲音檔案
            const audio = document.createElement("audio");
            audio.src = json.audio_file;
            audio.play();
        }
    });
}