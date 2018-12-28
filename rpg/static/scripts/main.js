$('#btnMonstros').click(function() {
    removerVisao();
    $('#monstrosDiv').removeClass("nVer");
});

$('#btnMapa').click(function() {
    removerVisao();
    $('#mapasDiv').removeClass("nVer");
});

$('#btnHabilidade').click(function() {
    removerVisao();
    $('#habilidadesDiv').removeClass("nVer");
});

$('#btnClasse').click(function() {
    removerVisao();
    $('#classesDiv').removeClass("nVer");
});

$('#btnRaca').click(function() {
    removerVisao();
    $('#racasDiv').removeClass("nVer");
});

function removerVisao(){
    $('#monstrosDiv').addClass("nVer");
    $('#mapasDiv').addClass("nVer");
    $('#habilidadesDiv').addClass("nVer");
    $('#classesDiv').addClass("nVer");
    $('#racasDiv').addClass("nVer");
}