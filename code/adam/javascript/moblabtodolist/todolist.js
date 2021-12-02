var close, myNodelist, span, txt
let itemsArray = []


const data = JSON.parse(localStorage.getItem('items'))


myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
    span = document.createElement("SPAN");
    txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
    }
}
function myLoad() {
    console.log("it works")
    const data = JSON.parse(localStorage.getItem('items')).value
    var i;
    for (i = 0; i < itemsArray.length; i++) {
        data[i].document.createElement("li")
    var list_item = document.createElement("li");
    // var inputValue = document.getElementById(data).value;
    var new_line = document.createTextNode(data[i]);
    // var done_list = document.getElementById("todo_list")
    document.getElementById("todo_list").appendChild(data[i])
    list_item.appendChild(new_line)

}}
// function mySave() {
//     var myContent = document.getElementById("enter_item").value;
//     localStorage.setItem("enter_item", myContent);
//   }

myLoad()


// Create a new list item when clicking on the "Add" button
function newToDo() {
    let itemsArray = localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : [];


    var list_item = document.createElement("li");
    var inputValue = document.getElementById("enter_item").value;
    var new_line = document.createTextNode(inputValue);
    var done_list = document.getElementById("done_list")
    const input = document.getElementById("enter_item")
    itemsArray.push(input.value)
    localStorage.setItem('items', JSON.stringify(itemsArray))
    const data = JSON.parse(localStorage.getItem('items'))
    list_item.appendChild(new_line);
    
    // When you click on it, the line moves to the done list
    list_item.addEventListener('click', function() {
        document.getElementById("done_list").appendChild(list_item)
        // We want to move the item back to the to do list
        if (done_list.contains(list_item)) {
            list_item.addEventListener('click', function() {
                document.getElementById('todo_list').appendChild(list_item)
            })
        }
    })
    // You must not try to add a blank entry
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        document.getElementById("todo_list").appendChild(list_item);
    }
    // This makes the text field for the user empty again
    document.getElementById("enter_item").value = "";
    
    data.forEach((element) => {
        // alert(element)
    })
    // Create a spot on the line for the x button
    var span = document.createElement("SPAN");
    // use the u00D7 Unicode for the x button https://www.htmlsymbols.xyz/unicode/U+00D7
    var txt = document.createTextNode("\u00D7");
    // Call it 'close' because the freaking example I looked at did so and that's that ;p
    span.className = "close";
    // Append the x to the span
    span.appendChild(txt);
    // Here is where we add the x to delete the item to the section above where we made the line 
    list_item.appendChild(span);

  

    // TA DA! The item is created at this point

    // This foor loop will take anything we click the x on and instead of deleting it, it will just hide it
    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
        }
    }
}