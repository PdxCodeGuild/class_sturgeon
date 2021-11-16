var close, myNodelist, span, txt

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


// Create a new list item when clicking on the "Add" button
function newToDo() {
    var list_item = document.createElement("li");
    var inputValue = document.getElementById("enter_item").value;
    var new_line = document.createTextNode(inputValue);
    var done_list = document.getElementById("done_list")
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