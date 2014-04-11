function Repositories(endpoint) {

	this.get = function() {
		$.getJSON('repositories/', this.render);
	};

	this.render = function(obj) {
		var el = $('#repo-line').html();
		var temp = '';
		for (var r in obj) {
			temp += _.template(el, {repo : obj[r]});
		}
		$('#repositories').html(temp);
		console.log("Repositories Rendered");
	};
}

function Issues() {

	this.currentPage = 0;

	this.get = function() {
		this.currentPage++;
		var pageString = '?page=' + this.currentPage + '&per_page=20';
		$.getJSON('https://api.github.com/repos/symfony/symfony/issues' + pageString, this.render);
		console.log("Get from issues");
	};

	this.render = function(obj) {
		console.log(obj);
		var el = $('#issue-line').html();
		var temp = '';
		for (var r in obj) {
			temp += _.template(el, {repo : obj[r]});
		}
		$('#issues').append(temp);
		console.log("Repositories Issues");
		console.log("Rendering issues");
	};
}

function Propositions() {

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

	repositories: new Repositories(),
	issues: new Issues(),

	init: function() {

		console.log("wallet app started");
	},

	getRepositories: function() {
		this.repositories.get();
	},

	getIssues: function(page) {
		this.issues.get();
	}
};


