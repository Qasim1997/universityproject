$('.plus-cart').click(function () {
    console.log("Plus clicked")
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log(id)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id:id
        },
        dataType: 'json',
        success: function (data) {
            console.log(data)
            console.log("success")

            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
        }


    })
})


$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log(id)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        dataType: 'json',
        success: function (data) {
            console.log(data)
            eml.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
        }
    })
})

$('.remove-cart').click(function () {
    
    var id = $(this).attr("pid").toString();
    var eml = this
    console.log(id)
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log(data)
            console.log("delete")
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})

