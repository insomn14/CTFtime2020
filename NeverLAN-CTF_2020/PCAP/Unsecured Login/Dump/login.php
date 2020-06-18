<!DOCTYPE html>
<html>
	<head>
		<title>My Awesome Login Page</title>
		<link rel="stylesheet" href="css/bulma.min.css"/>
		<link rel="stylesheet" href="css/main.css"/>
	</head>
	<body>
		<nav class="navbar" role="navigation" aria-label="main navigation">
			<div class="navbar-brand">
				<a class="navbar-item" href="/">
					<img src="https://cdn.neverlanctf.com/Logo-dark.png" alt="My Awesome Site"/>
				</a>
				<a role="button" class="navbarp-burger" aria-label="menu" aria-expanded="false">
					<span aria-hidden="true"></span>
					<span aria-hidden="true"></span>
					<span aria-hidden="true"></span>
				</a>
			</div>
		</nav>
		<main>
			<div class="container">
				<div class="columns is-centered">
					<div class="column is-one-third">
						<section class="section">
							<div class="container">
								
			<h1 class="title">Please Login Here</h1>
			<form method="post">
				<div class="field">
					<p class="control has-icons-left">
						<input class="input" type="text" placeholder="Username" name="user">
						<span class="icon is-small is-left">
							<i class="fas fa-user"></i>
						</span>
					</p>
				</div>
				<div class="field">
					<p class="control has-icons-left">
						<input class="input" type="password" placeholder="Password" name="pass">
						<span class="icon is-small is-left">
							<i class="fas fa-lock"></i>
						</span>
					</p>
				</div>
				<div class="field">
					<p class="control">
						<button class="button is-success">
							Login
						</button>
					</p>
				</div>
			</form>							</div>
						</section>
					</div>
				</div>
			</div>
		</main>
		<footer class="footer">
			<div class="content has-text-centered">
				<p>
					<strong>My Awesome website</strong> by <a href="https://neverlanctf.com">Some Cool People</a>
				</p>
			</div>
		</footer>
	</body>
</html>
