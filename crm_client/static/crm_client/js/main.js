
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
           $('.add-modal-button').prop('disabled', true);
           let error = $(data).find('.errorlist'); //Проверка на ошибки в форме
           if (error.length) {
               $("#myFormAddAuto").html($(data).find('.add-auto'));
               alert('Error!!!');
           }
           else {
               $(".add-auto").html($(data).find('#myFormAddAuto'));
               $(".add-client").html($(data).find('#myNameForm'));
           }

        }
    });


});

//Событие загрузки документа
$(document).ready(function() {
    //Делаем кнопку "Сохранить" активной
    let body = $('body');
    $('.add-modal-button').prop('disabled', true);
    //Событие изменения выбора марки
    body.on('change', '.add_brand_choice', function () {
    // Скрытие поля марки
        let choice = $('#id_auto_brand');
        if (choice.val() === '6') {
            $('.new_add_brand_label').show();

        } else {
            $('.new_add_brand_label').hide();
        }
        //Скрытие поля модели авто
        if (choice.val() !== ''){
            $('.new_add_model_label').show();
        }
        else {
            $('.new_add_model_label').hide();
        }

    });
    //Собитие изменения текстовых полей формы скрытие появление кнопки
    body.on('keyup', '#id_add_auto_brand, #id_add_model', function () {
        // $('#id_add_auto_brand, #id_add_model').keyup(function () {
        let new_brand = $('#id_add_auto_brand');
        let new_model = $('#id_add_model');


        if (new_brand.val().length && new_model.val().length) {
            $('.add-modal-button').prop('disabled', false);
        } else {
            $('.add-modal-button').prop('disabled', true);
        }


    //Делаем кнопку активной\неактивной если выбрана существующая марка
        let choice = $('#id_auto_brand').val();

        if (choice !== '6' && choice !== '' ) {
            if (new_model.val().length) {
                $('.add-modal-button').prop('disabled', false);
            } else {
                $('.add-modal-button').prop('disabled', true);
            }

        }
        // else {
        //     if (new_model.val().length){
        //         $('.add-modal-button').prop('disabled', false);
        //     }
        //
        // }


    });

    // body.on('ready', '#myFormAddAuto', function () {
    //     $('.add-modal-button').prop('disabled', true);
    // });
    //Сброс полей формы при нажатии клавиши закрыть
    body.on('click', '.add-auto-close, .add-auto-back', function () {
        $('#myFormAddAuto')[0].reset();
    });

    // body.on('keyup', '#seed_one',function () {

//поиск
    body.on('click', '.ser', function () {
        let form = $('#form-search').serialize() + "&method=search" ;

    $.ajax({
    url: "/client-base/",
    type: 'POST',
    data: form,
        success: function(data) {
            // $('.add-modal-button').prop('disabled', true);
            let error = $(data).find('.errorlist'); //Проверка на ошибки в форме
            if (error.length) {
                $("#myFormAddAuto").html($(data).find('.add-auto'));
                alert('Error!!!');
            }
            else {
                console.log(data);
                $(".wrp").html($(data).find('.table'));
                $('.ert').html($(data).find('.ert'));
            }
        }
    });

});

//Сброс поиска
 body.on('click', '.reset-search', function () {

    $.ajax({
        url: "/client-base/",
        type: 'GET',
        // data: form,
        success: function (data) {
            $(".wrp").html($(data).find('.table'));
            $('#form-search')[0].reset();
        }
    });
 });

//закрытие
});

