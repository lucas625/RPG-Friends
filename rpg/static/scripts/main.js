$('#btnMonstros').click(function() {
    removerVisao();
    $('#monstrosDiv').removeClass("nVer");
});

$('#btnMapa').click(function() {
    removerVisao();
});

function removerVisao(){
    $('#monstrosDiv').addClass("nVer");
}