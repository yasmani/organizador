document.addEventListener("DOMContentLoaded", function () {
    // Seleccionamos solo los enlaces dentro del menú lateral (sidebar)
    let sidebar = document.querySelector(".main-sidebar");
    let navLinks = sidebar.querySelectorAll(".nav-item .nav-link");

    navLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            // Removemos la clase 'active' solo de los enlaces dentro del sidebar
            navLinks.forEach(function (item) {
                item.classList.remove("active");
            });

            // Agregamos la clase 'active' al enlace que se hizo clic
            this.classList.add("active");
        });
    });
});



$(document).ready(function(){
    $("#area").change(function(){
        var identificador = $(this).val();

        

       

        $.ajax({
            url: "/obtener_solicitudes/",
            data: {'identificador': identificador},
            dataType: 'json',
            success: function(data){
                 
                var selectHTML = '<select class="form-control form-control-sm" name="solicitud" required>';
                selectHTML += '<option selected disabled>SELECCIONAR SOLICITUD</option>';

                $.each(data, function(index, solicitud){
                    selectHTML += '<option value="' + solicitud.id_rel + '">' + solicitud.solicitud + '</option>';
                });

                selectHTML += '</select>';

                $("#f1").html(selectHTML);
            }
        });
    });
});


