$(document).ready(function() {
    $("#save").css("display","none");
    $("#cancel").css("display","none");
    $("#editOutcomes").click(function(){
        $(".edit").prop("disabled", false);
        $('.editButton').removeClass('btn-secondary').addClass('btn-primary');
        $("#save").css("display","inline");
        $("#cancel").css("display","inline");
        $("#editOutcomes").css("display","none");
    });
    $("#cancel").click(function(){
      $(".edit").prop("disabled", true);
      $('.editButton').removeClass('btn-primary').addClass('btn-secondary');
      $("#save").css("display","none");
      $("#cancel").css("display","none");
      $("#editOutcomes").css("display","inline");
  });
    $('.opt').click(function(){
        var val = $(this).html();
        $('#searchDate').val(val);
    });
    
});
jQuery(function($){
  $("#date").mask("9999-99");
  $('#searchDate').mask("9999-99");

  $('.pagination').html('');
  var trnum = 0;
  var maxRows = 20;
  var totalRows = $('#listCrimes tbody tr').length;
  $('#listCrimes tr:gt(0)').each(function(){
    trnum++;
    if(trnum > maxRows){
      $(this).hide();
    }
    if(trnum <= maxRows){
      $(this).show();
    }
  });
  if(totalRows > maxRows){
    var pageNum = Math.ceil(totalRows/maxRows);
    for(var i=1;i<=pageNum;){
      $('.pagination').append('<li class="page-item" data-page="'+i+'"><a class="page-link" href="#">'+ i++ +'</a></li>').show();
    }
  }
  $('.pagination li:first-child').addClass('active');
  $('.pagination li').on('click',function(){
    var pageNum = $(this).attr('data-page');
    var trIndex = 0;
    $('.pagination li').removeClass('active');
    $(this).addClass('active');
    $('#listCrimes tr:gt(0)').each(function(){
      trIndex++;
      if(trIndex > (maxRows*pageNum) || trIndex <= ((maxRows*pageNum)-maxRows)){
        $(this).hide();
      }else{
        $(this).show();
      }
    });
  });
});
 