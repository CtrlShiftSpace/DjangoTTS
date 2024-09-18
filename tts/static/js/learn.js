$(document).ready(function (){
    // 按下聆聽按鈕
    $('#btn-trans-audio').on('click', transAudioHandler);
    // 按下單字旁的念法
    $('#word-catch-table').on('click', '.btn-word-repeat', repeatWordHandler);
});

function transAudioHandler(e) {
    let comm_text = $("#input-trans-audio").val();
    // 未輸入單字或句子
    if (comm_text.trim() == "") {
        return;
    }
}

function repeatWordHandler(e) {
    let comm_text = $(this).attr("data-word");
    if (comm_text.trim() == "") {
        return;
    }
    ajaxEdgeTTS(comm_text);
}

function ajaxEdgeTTS(comm_text) {
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