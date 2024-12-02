
// Клик по флажку
// $(".form-check-input").click(function(event){
$(document).on('click',".form-check-input", function() {
// проверка есть хотя бы 1 выделенный чекбокс
     if ($(".form-check-input:checked").length > 0){
// делаем кнопку активной
         $(".update-button").prop('disabled', false);
         $(".delete-button").prop('disabled', false);
         $(".delete-select-button").prop('disabled', false);
// иначе делаем кнопку неактивной
     }else {
         $(".update-button").prop('disabled', true);
         $(".delete-button").prop('disabled', true);
         $(".delete-select-button").prop('disabled', true);
     }
// Проверка что выделенных чекбоксов не больше одного
    if ($(".form-check-input:checked").length > 1){
        $(".update-button").prop('disabled', true);
    }
    });
// Клик по кнопке
$(".select-button").click(function() {
    $('.form-check-input').prop("checked", true);
    $(".delete-select-button").prop('disabled', false);
    $(".update-button").prop('disabled', true);
    $(".delete-button").prop('disabled', false);

  });
$(".delete-select-button").click(function() {
    $('.form-check-input').prop("checked", false);
    $(".update-button").prop('disabled', true);
    $(".delete-button").prop('disabled', true);
    $(".delete-select-button").prop('disabled', true);
});

// Функция поиска выделенных записей
function search_checkbox(){
    // let data = $(".form-check-input:checked");
    let map = [];
    check = $('input[type=checkbox]:checked').each(function (){
       map.push($(this).val());
    });

    // check.each({
    //     alert()
    // })



    console.log(map);
    return map;
}


// Удаление записи
$(".delete-button").click(function() {
    let tablecheck = search_checkbox();
    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    let data = {
        'csrfmiddlewaretoken':csrftoken,
        'pk':tablecheck,
        'method':'delete',
    }

    $.ajax({
    url: "/client-base/",
    type: 'POST',
    data: data,
    success: function(data){
                $(".wrp").html($(data).find('.table'));//Замена части страницы
                $(".update-button").prop('disabled', true);//Делает кнопки неактивными
                $(".delete-button").prop('disabled', true);
                $(".delete-select-button").prop('disabled', true);
                // $('.information-row').append( "Записи успешно удалены" );
                $('.ert').html($(data).find('.ert'));
                setTimeout(fade_out, 5000);//Удаление сообщения
                function fade_out() {
                    $(".ert").empty();
                }
            }
    });
});

// Добавление записи
$(".add-button").click(function() {

    let form = $('#myNameForm').serialize() + "&method=add" ;
    $.ajax({
    url: "/client-base/",
    type: 'POST',
    data: form,
    success: function(data){

                let error = $(data).find('.errorlist'); //Проверка на ошибки в форме
                if (error.length) {
                    $(".add-client").html($(data).find('#myNameForm'));
                }
                else{
                    $(".wrp").html($(data).find('.table'));//Замена части страницы
                    // $('#myNameForm')[0].reset();//очистка полей таблицы
                    $('#staticBackdrop').modal('hide');//закрытие модального окна
                    $(".add-client").html($(data).find('#myNameForm'));
                    $('.ert').html($(data).find('.ert'));
                    setTimeout(fade_out, 5000);//Удаление сообщения
                    function fade_out() {
                        $(".ert").empty();
                    }
                }

            },
            error:function (data){
                alert("Ошибка! Что-то пошло не так, попробуйте снова");
            }

    });

});

//Добавление автомобиля
$(".add-modal-button").click(function() {
    let form = $('#myFormAddAuto').serialize() + "&method=add_auto" ;//добавление словаря с названием метода

    $.ajax({
    url: "/client-base/",
    type: 'POST',
    data: form,
    success: function(data) {
           let error = $(data).find('.errorlist'); //Проверка на ошибки в форме
           if (error.length) {
                    $(".add-auto").html($(data).find('#myNameForm'));
           }
           else {
               $("#myFormAddAuto").html($(data).find('.message-auto'));
           }

        }
    });


});
