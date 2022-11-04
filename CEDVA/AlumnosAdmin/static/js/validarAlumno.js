const $formRegistroAlumno = document.getElementById('formRegistroAlumno');

const $matricula = document.getElementById('matricula');
const $nombreA = document.getElementById('nombreA');
const $apellidoPA = document.getElementById('apellidoPA');
const $apellidoMA = document.getElementById('apellidoMA');
const $edad = document.getElementById('edad');
const $inicioCurso = document.getElementById('inicioCurso');
const $finalCurso = document.getElementById('finalCurso');
const $convenio = document.getElementById('convenio');
const $calle = document.getElementById('calle');
const $colonia = document.getElementById('colonia');
const $nombreT = document.getElementById('nombreT');
const $apellidoPT = document.getElementById('apellidoPT');
const $apellidoMT = document.getElementById('apellidoMT');
const $telefono = document.getElementById('telefono');



(function (){
	$formRegistroAlumno.addEventListener('submit', function(e){
		let matri = String($matricula.value).trim();
		if (matri.length===0) {
			alert("La matricula no puede ir vacio. Verificar Datos Generales");
			e.preventDefault();
		}

		let nomA = String($nombreA.value).trim();
		if (nomA.length===0) {
			alert("El nombre no puede ir vacio. Verificar Datos Generales");
			e.preventDefault();
		}

		let appA = String($apellidoPA.value).trim();
		if (appA.length===0) {
			alert("El apellido paterno no puede ir vacio. Verificar Datos Generales");
			e.preventDefault();
		}

		let appM = String($apellidoMA.value).trim();
		if (appA.length===0) {
			alert("El apellido materno no puede ir vacio. Verificar Datos Generales");
			e.preventDefault();
		}

		let conv = String($convenio.value).trim();
		if (conv.length===0) {
			alert("Convenio no puede ir vacio. Verificar Datos Generales");
			e.preventDefault();
		}

		let calle = String($calle.value).trim();
		if (calle.length===0) {
			alert("Calle no puede ir vacio. Verificar Domicilio");
			e.preventDefault();
		}

		let colonia = String($colonia.value).trim();
		if (colonia.length===0) {
			alert("Colonia no puede ir vacio. Verificar Domicilio");
			e.preventDefault();
		}

		let delegacionM = String($delegacionMunicipio.value).trim();
		if (delegacionM.length===0) {
			alert("Delegación no puede ir vacio. Verificar Domicilio");
			e.preventDefault();
		}

		let nomT = String($nombreT.value).trim();
		if (nomT.length===0) {
			alert("Nombre del tutor no puede ir vacio. Verificar Tutor");
			e.preventDefault();
		}

		let appT = String($apellidoPT.value).trim();
		if (appT.length===0) {
			alert("Apellido paterno del tutor no puede ir vacio. Verificar Tutor");
			e.preventDefault();
		}

		let apmT = String($apellidoMT.value).trim();
		if (apmT.length===0) {
			alert("Apellido materno del tutor no puede ir vacio. Verificar Tutor");
			e.preventDefault();
		} 
		
	});

})();