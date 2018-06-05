$(function () {
	var selectSystem = document.getElementById('id_operatingSystem');
	var currentSystem = selectSystem.options[selectSystem.selectedIndex].value;
	changeSystem(currentSystem);


	$("#id_operatingSystem").change(function () {
		var currentSystem = this.options[this.selectedIndex].value;
		var collapse = document.getElementById('helpHostID');
		changeSystem(currentSystem);
	});

	$('#sendForm').click(function(){

		var reg = new RegExp("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$");
		if(!reg.test($("#id_hostID").val())){
			document.getElementById("id_hostID").setCustomValidity("L'hostID n'est pas au bon format (ex : 17:AE:45:RE:4D:8D, 17-AE-45-RE-4D-8D).");
		}
		else{
			document.getElementById("id_hostID").setCustomValidity("");
		}

		reg = new RegExp("^0[0-9]{9}$");
		if(!reg.test($("#id_telephone").val())){
			document.getElementById("id_telephone").setCustomValidity("Le numéro de téléphone n'est pas au bon format.");
		}
		else{
			document.getElementById("id_telephone").setCustomValidity("");
		}

	});


});


function changeSystem(system) {
	var helpHostId = document.getElementById("helpText"),
	divWindow = document.getElementById("Windows"),
	divLinux = document.getElementById("Linux"),
	divMacOs = document.getElementById("MacOs");
	switch(system)
	{
		case 'MacOS' :
			if(divWindow.style.display == 'initial')
				divWindow.style.display = 'none';
			if(divLinux.style.display == 'initial')
				divLinux.style.display = 'none';
			if(divMacOs.style.display == 'none')
				divMacOs.style.display = 'initial';
			break;
		case 'Linux' :
			if(divWindow.style.display == 'initial')
				divWindow.style.display = 'none';
			if(divLinux.style.display == 'none')
				divLinux.style.display = 'initial';
			if(divMacOs.style.display == 'initial')
				divMacOs.style.display = 'none';
			break;
		case 'Windows' :
			if(divWindow.style.display == 'none')
				divWindow.style.display = 'initial';
			if(divLinux.style.display == 'initial')
				divLinux.style.display = 'none';
			if(divMacOs.style.display == 'initial')
				divMacOs.style.display = 'none';
			break;
	}
}
