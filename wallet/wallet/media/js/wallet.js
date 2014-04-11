function Repositories(endpoint) {
	this.server = 'http://localhost:8000/';
	this.get = function() {
		$.getJSON(this.server + 'repositories/', this.render);
	};

	this.getMy = function() {
		$.get(this.server + 'my_repositories/', this.render_my);
	};

	this.add = function(owner, repo, token) {
		var that = this;
		$.post(this.server + 'repositories/', {'owner': owner, 'repo': repo, 'csrfmiddlewaretoken': token},
			function(data) {
				that.getMy();
				that.get();
			},'json');
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

	this.render_my = function(obj) {
		obj = JSON.parse(obj);
		console.log(obj);
		$el = $('#my-repo-list');
		$el.html('');
		for (var r in obj) {
			$el.append('<li>' + obj[r]['fields']['fullname'] + '</li>');
		}
	};
}

function Issues() {

	this.currentPage = 0;

	this.get = function(fullname) {
		this.currentPage++;
		var pageString = '?state=open&page=' + this.currentPage + '&per_page=20';
		$.getJSON('https://api.github.com/repos/' + fullname + '/issues' + pageString, this.render);
		console.log("Get from issues");
	};

	this.search = function(fullname) {

		var input = $("#highlight_input").val();
		var id = input.substring(input.lastIndexOf('/'));
		$.getJSON('https://api.github.com/repos/' + fullname + '/issues' + id, this.render);
	};

	this.render = function(obj) {
		console.log(obj);
		var el = $('#issue-line').html();
		var temp = '';

		if(obj.length > 1) {
			for (var r in obj) {
				temp += _.template(el, {repo : obj[r]});
			}
			$('#issues').append(temp);
		} else {
			temp = _.template(el, {repo : obj});
			$('#issues').html(temp);
		}
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

	addRepository: function() {
		var input = $('#add_repository_url').val();
		var repo = input.substring(input.lastIndexOf('/') + 1);
		var owner = input.split('/').slice(-2)[0];
		var token = $('input[name=csrfmiddlewaretoken]').val();
		$('#add_repository_url').val('');
		this.repositories.add(owner, repo, token);
	},

	getIssues: function() {
		this.issues.get(this.repoFullName);
	}
};


