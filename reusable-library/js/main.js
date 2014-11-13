function validateForm() {
    var sex = document.forms["form"]["sex"].value,
    	weight = document.forms["form"]["weight"].value,
    	drink = document.forms["form"]["drink"].value,
    	number = document.forms["form"]["number"].value,
    	hours = document.forms["form"]["hours"].value;
    	
    if (sex==null || sex=="") {
        alert("First name must be filled out");
        return false;
    }
}