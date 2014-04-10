function Repositories(endpoint) {

	this.server = endpoint;

	this.get = function() {
		console.log("Get from endpoint");
	};

	this.render = function(obj) {
		console.log("Rendering repositories");
	};

}

function Issues(endpoint) {
	this.server = endpoint;

	this.get = function() {
		console.log("Get from issues");
	};

	this.render = function() {
		console.log("Rendering issues");
	};
}

function Propositions(endpoint) {
	this.server = endpoint;

	this.get = function() {
		console.log("Get from propositions");
	};

	this.create = function() {

	};

	this.render = function() {
		console.log("Rendering propositions");
	};
};

var wallet = {

	endpoint: 'http://localhost:8000', 
	repositories: new Repositories(this.endpoint),
	issues: new Issues(this.endpoint),

	initEvents: function() {
		console.log("wallet app started");
		this.repositories.get();
	}

};

wallet.init();