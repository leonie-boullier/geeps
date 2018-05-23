$(function () {
	var selectSystem = document.getElementById('id_operatingSystem');
	var currentSystem = selectSystem.options[selectSystem.selectedIndex].value;
	changeSystem(currentSystem);
	
	$("#id_operatingSystem").change(function () {
		var currentSystem = this.options[this.selectedIndex].value;
		var collapse = document.getElementById('helpHostID');
		changeSystem(currentSystem);
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
