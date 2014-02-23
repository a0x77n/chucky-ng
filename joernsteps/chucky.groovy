




<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>joern-projects/joernsteps/chucky.groovy at master · a0x77n/joern-projects · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="a0x77n/joern-projects" name="twitter:title" /><meta content="joern-projects - Projects based on joern" name="twitter:description" /><meta content="https://2.gravatar.com/avatar/084c582f019b1358c9c8de35a3c7c023?d=https%3A%2F%2Fidenticons.github.com%2F0b3eda03cf5e16afedf7d4ab8d14be0d.png&amp;r=x&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://2.gravatar.com/avatar/084c582f019b1358c9c8de35a3c7c023?d=https%3A%2F%2Fidenticons.github.com%2F0b3eda03cf5e16afedf7d4ab8d14be0d.png&amp;r=x&amp;s=400" property="og:image" /><meta content="a0x77n/joern-projects" property="og:title" /><meta content="https://github.com/a0x77n/joern-projects" property="og:url" /><meta content="joern-projects - Projects based on joern" property="og:description" />

    <meta name="hostname" content="github-fe133-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 2.1.0p0-github-tcmalloc (87c9373a41) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="4D08A32F:5647:FC96C5:530A67CD" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="3airfXq2WjfjLegH+2vlCHJGJrNmUeiXNa19rNmVOAI=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-22cc6aa8138609ccbf0c65025e153af581662ef6.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-dd234c178c0a2e0769bab2b5c636ce8f3fc1f02a.css" media="all" rel="stylesheet" type="text/css" />
    
    


      <script crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/frameworks-01ab94ef47d6293597922a1fab60e274e1d8f37e.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/github-a8a26802e0e7283b39ee4507af78950399f2a5d1.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="df411d3c97b15f5ab1e253f83d14f069">

        <link data-pjax-transient rel='permalink' href='/a0x77n/joern-projects/blob/bb6d51cc4df752530b2df81e54fe3fbd8bb85d44/joernsteps/chucky.groovy'>

  <meta name="description" content="joern-projects - Projects based on joern" />

  <meta content="6086764" name="octolytics-dimension-user_id" /><meta content="a0x77n" name="octolytics-dimension-user_login" /><meta content="16407892" name="octolytics-dimension-repository_id" /><meta content="a0x77n/joern-projects" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="16407892" name="octolytics-dimension-repository_network_root_id" /><meta content="a0x77n/joern-projects" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/a0x77n/joern-projects/commits/master.atom" rel="alternate" title="Recent Commits to joern-projects:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production linux vis-public page-blob tipsy-tooltips">
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fa0x77n%2Fjoern-projects%2Fblob%2Fmaster%2Fjoernsteps%2Fchucky.groovy">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey=" s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="a0x77n/joern-projects"
      data-branch="master"
      data-sha="e906f3d7e6e0cde874475d4fcce007d37fa6a4bf"
  >

    <input type="hidden" name="nwo" value="a0x77n/joern-projects" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fa0x77n%2Fjoern-projects"
    class="minibutton with-count js-toggler-target star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to use this feature" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/a0x77n/joern-projects/stargazers">
      1
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fa0x77n%2Fjoern-projects"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/a0x77n/joern-projects/network" class="social-count">
        1
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/a0x77n" class="url fn" itemprop="url" rel="author"><span itemprop="title">a0x77n</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/a0x77n/joern-projects" class="js-current-repository js-repo-home-link">joern-projects</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/a0x77n/joern-projects" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /a0x77n/joern-projects">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/a0x77n/joern-projects/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /a0x77n/joern-projects/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/a0x77n/joern-projects/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /a0x77n/joern-projects/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/a0x77n/joern-projects/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /a0x77n/joern-projects/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/a0x77n/joern-projects/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /a0x77n/joern-projects/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/a0x77n/joern-projects/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /a0x77n/joern-projects/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/a0x77n/joern-projects.git" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/a0x77n/joern-projects.git" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/a0x77n/joern-projects" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/a0x77n/joern-projects" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



                <a href="/a0x77n/joern-projects/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:fc84b7f49de1816dcd2f6a9093c9c528 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/a0x77n/joern-projects/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/a0x77n/joern-projects/blob/master/joernsteps/chucky.groovy"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/a0x77n/joern-projects" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">joern-projects</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/a0x77n/joern-projects/tree/master/joernsteps" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">joernsteps</span></a></span><span class="separator"> / </span><strong class="final-path">chucky.groovy</strong> <span aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="joernsteps/chucky.groovy" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit file-history-tease">
    <img alt="Alwin Maier" class="main-avatar js-avatar" data-user="6086764" height="24" src="https://2.gravatar.com/avatar/084c582f019b1358c9c8de35a3c7c023?d=https%3A%2F%2Fidenticons.github.com%2F0b3eda03cf5e16afedf7d4ab8d14be0d.png&amp;r=x&amp;s=140" width="24" />
    <span class="author"><a href="/a0x77n" rel="author">a0x77n</a></span>
    <time class="js-relative-date" data-title-format="YYYY-MM-DD HH:mm:ss" datetime="2014-02-07T03:24:51-08:00" title="2014-02-07 03:24:51">February 07, 2014</time>
    <div class="commit-title">
        <a href="/a0x77n/joern-projects/commit/bb6d51cc4df752530b2df81e54fe3fbd8bb85d44" class="message" data-pjax="true" title="Reworked tainting steps">Reworked tainting steps</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Alwin Maier" class=" js-avatar" data-user="6086764" height="24" src="https://2.gravatar.com/avatar/084c582f019b1358c9c8de35a3c7c023?d=https%3A%2F%2Fidenticons.github.com%2F0b3eda03cf5e16afedf7d4ab8d14be0d.png&amp;r=x&amp;s=140" width="24" />
            <a href="/a0x77n">a0x77n</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>95 lines (87 sloc)</span>
          <span class="meta-divider"></span>
        <span>2.186 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/a0x77n/joern-projects/raw/master/joernsteps/chucky.groovy" class="button minibutton " id="raw-url">Raw</a>
            <a href="/a0x77n/joern-projects/blame/master/joernsteps/chucky.groovy" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/a0x77n/joern-projects/commits/master/joernsteps/chucky.groovy" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
        <div class="blob-wrapper data type-groovy js-blob-data">
        <table class="file-code file-diff tab-size-8">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>

            </td>
            <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;subTrees&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC2'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC3'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC4'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="mi">1</span><span class="o">){</span><span class="n">it</span><span class="o">.</span><span class="na">loops</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="o">}{</span><span class="kc">true</span><span class="o">}</span></div><div class='line' id='LC5'><span class="o">});</span></div><div class='line' id='LC6'><br/></div><div class='line' id='LC7'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;taint&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC8'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC9'>	<span class="o">.</span><span class="na">copySplit</span><span class="o">(</span><span class="n">_</span><span class="o">().</span><span class="na">taintUpwards</span><span class="o">(),</span> <span class="n">_</span><span class="o">().</span><span class="na">taintDownwards</span><span class="o">())</span></div><div class='line' id='LC10'>	<span class="o">.</span><span class="na">fairMerge</span><span class="o">()</span></div><div class='line' id='LC11'><span class="o">});</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;taintUpwards&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC14'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC15'>	<span class="o">.</span><span class="na">as</span><span class="o">(</span><span class="s1">&#39;back&#39;</span><span class="o">)</span></div><div class='line' id='LC16'>	<span class="o">.</span><span class="na">copySplit</span><span class="o">(</span><span class="n">_</span><span class="o">().</span><span class="na">hasArguments</span><span class="o">(),</span> <span class="n">_</span><span class="o">().</span><span class="na">isAssignedBy</span><span class="o">())</span></div><div class='line' id='LC17'>	<span class="o">.</span><span class="na">fairMerge</span><span class="o">()</span></div><div class='line' id='LC18'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="s1">&#39;back&#39;</span><span class="o">){</span><span class="kc">true</span><span class="o">}{</span><span class="kc">true</span><span class="o">}</span></div><div class='line' id='LC19'>	<span class="o">.</span><span class="na">dedup</span><span class="o">()</span></div><div class='line' id='LC20'><span class="o">});</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;taintDownwards&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC23'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC24'>	<span class="o">.</span><span class="na">as</span><span class="o">(</span><span class="s1">&#39;back&#39;</span><span class="o">)</span></div><div class='line' id='LC25'>	<span class="o">.</span><span class="na">copySplit</span><span class="o">(</span><span class="n">_</span><span class="o">().</span><span class="na">isArgumentOf</span><span class="o">(),</span> <span class="n">_</span><span class="o">().</span><span class="na">assigns</span><span class="o">())</span></div><div class='line' id='LC26'>	<span class="o">.</span><span class="na">fairMerge</span><span class="o">()</span></div><div class='line' id='LC27'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="s1">&#39;back&#39;</span><span class="o">){</span><span class="kc">true</span><span class="o">}{</span><span class="kc">true</span><span class="o">}</span></div><div class='line' id='LC28'>	<span class="o">.</span><span class="na">dedup</span><span class="o">()</span></div><div class='line' id='LC29'><span class="o">});</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;isArgumentOf&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC32'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC33'>	<span class="o">.</span><span class="na">in</span><span class="o">(</span><span class="s1">&#39;USE&#39;</span><span class="o">)</span></div><div class='line' id='LC34'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;Argument&#39;</span> <span class="o">}</span></div><div class='line' id='LC35'>	<span class="o">.</span><span class="na">in</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC36'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="mi">1</span><span class="o">){</span> <span class="n">it</span><span class="o">.</span><span class="na">object</span><span class="o">.</span><span class="na">type</span> <span class="o">!=</span> <span class="s1">&#39;CallExpression&#39;</span> <span class="o">}</span></div><div class='line' id='LC37'>	<span class="o">.</span><span class="na">as</span><span class="o">(</span><span class="s1">&#39;callExpression&#39;</span><span class="o">)</span></div><div class='line' id='LC38'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC39'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;Identifier&#39;</span> <span class="o">}</span></div><div class='line' id='LC40'>	<span class="o">.</span><span class="na">sideEffect</span><span class="o">{</span> <span class="n">callee</span> <span class="o">=</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">}</span></div><div class='line' id='LC41'>	<span class="o">.</span><span class="na">back</span><span class="o">(</span><span class="s1">&#39;callExpression&#39;</span><span class="o">)</span></div><div class='line' id='LC42'>	<span class="o">.</span><span class="na">in</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC43'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="mi">1</span><span class="o">){</span><span class="kc">true</span><span class="o">}{</span><span class="n">it</span><span class="o">.</span><span class="na">object</span><span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;USE&#39;</span><span class="o">).</span><span class="na">count</span><span class="o">()</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="o">}</span></div><div class='line' id='LC44'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;USE&#39;</span><span class="o">)</span></div><div class='line' id='LC45'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">==</span> <span class="n">callee</span> <span class="o">}</span></div><div class='line' id='LC46'><span class="o">});</span></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;assigns&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC49'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC50'>	<span class="o">.</span><span class="na">sideEffect</span><span class="o">{</span> <span class="n">symbol</span> <span class="o">=</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">}</span></div><div class='line' id='LC51'>	<span class="o">.</span><span class="na">in</span><span class="o">(</span><span class="s1">&#39;USE&#39;</span><span class="o">)</span></div><div class='line' id='LC52'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">!=</span> <span class="s1">&#39;BasicBlock&#39;</span> <span class="o">}</span></div><div class='line' id='LC53'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC54'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="mi">1</span><span class="o">){</span> <span class="kc">true</span> <span class="o">}{</span> <span class="n">it</span><span class="o">.</span><span class="na">object</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;AssignmentExpr&#39;</span> <span class="o">}</span></div><div class='line' id='LC55'>	<span class="o">.</span><span class="na">as</span><span class="o">(</span><span class="s1">&#39;candidate&#39;</span><span class="o">)</span></div><div class='line' id='LC56'>	<span class="o">.</span><span class="na">outE</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC57'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span><span class="n">it</span><span class="o">.</span><span class="na">n</span> <span class="o">==</span> <span class="s1">&#39;1&#39;</span> <span class="o">}</span></div><div class='line' id='LC58'>	<span class="o">.</span><span class="na">inV</span><span class="o">()</span></div><div class='line' id='LC59'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC60'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="mi">1</span><span class="o">){</span><span class="kc">true</span><span class="o">}{</span><span class="n">it</span><span class="o">.</span><span class="na">object</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;Identifier&#39;</span><span class="o">}</span></div><div class='line' id='LC61'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span><span class="n">it</span><span class="o">.</span><span class="na">code</span><span class="o">.</span><span class="na">equals</span><span class="o">(</span><span class="n">symbol</span><span class="o">)}</span></div><div class='line' id='LC62'>	<span class="o">.</span><span class="na">back</span><span class="o">(</span><span class="s1">&#39;candidate&#39;</span><span class="o">)</span></div><div class='line' id='LC63'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;DEF&#39;</span><span class="o">)</span></div><div class='line' id='LC64'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">!=</span> <span class="s2">&quot;&quot;</span> <span class="o">}</span></div><div class='line' id='LC65'><span class="o">});</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;hasArguments&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC68'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC69'>	<span class="o">.</span><span class="na">sideEffect</span><span class="o">{</span> <span class="n">symbol</span> <span class="o">=</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">}</span></div><div class='line' id='LC70'>	<span class="o">.</span><span class="na">in</span><span class="o">(</span><span class="s1">&#39;USE&#39;</span><span class="o">)</span></div><div class='line' id='LC71'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">!=</span> <span class="s1">&#39;BasicBlock&#39;</span> <span class="o">}</span></div><div class='line' id='LC72'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC73'>	<span class="o">.</span><span class="na">loop</span><span class="o">(</span><span class="mi">1</span><span class="o">){</span><span class="kc">true</span><span class="o">}{</span><span class="n">it</span><span class="o">.</span><span class="na">object</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;CallExpression&#39;</span><span class="o">}</span></div><div class='line' id='LC74'>	<span class="o">.</span><span class="na">as</span><span class="o">(</span><span class="s1">&#39;candidate&#39;</span><span class="o">)</span></div><div class='line' id='LC75'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC76'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span><span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;Identifier&#39;</span> <span class="o">&amp;&amp;</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span><span class="o">.</span><span class="na">equals</span><span class="o">(</span><span class="n">symbol</span><span class="o">)</span> <span class="o">}</span></div><div class='line' id='LC77'>	<span class="o">.</span><span class="na">back</span><span class="o">(</span><span class="s1">&#39;candidate&#39;</span><span class="o">)</span></div><div class='line' id='LC78'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC79'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;ArgumentList&#39;</span> <span class="o">}</span></div><div class='line' id='LC80'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC81'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;Argument&#39;</span> <span class="o">}</span></div><div class='line' id='LC82'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;USE&#39;</span><span class="o">)</span></div><div class='line' id='LC83'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">!=</span> <span class="s2">&quot;&quot;</span> <span class="o">}</span></div><div class='line' id='LC84'><span class="o">});</span></div><div class='line' id='LC85'><br/></div><div class='line' id='LC86'><span class="n">Gremlin</span><span class="o">.</span><span class="na">defineStep</span><span class="o">(</span><span class="s1">&#39;isAssignedBy&#39;</span><span class="o">,</span> <span class="o">[</span><span class="n">Vertex</span><span class="o">,</span> <span class="n">Pipe</span><span class="o">],</span> <span class="o">{</span></div><div class='line' id='LC87'>	<span class="n">_</span><span class="o">()</span></div><div class='line' id='LC88'>	<span class="o">.</span><span class="na">sideEffect</span><span class="o">{</span> <span class="n">symbol</span> <span class="o">=</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">}</span></div><div class='line' id='LC89'>	<span class="o">.</span><span class="na">in</span><span class="o">(</span><span class="s1">&#39;DEF&#39;</span><span class="o">)</span></div><div class='line' id='LC90'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">type</span> <span class="o">==</span> <span class="s1">&#39;AssignmentExpr&#39;</span> <span class="o">}</span></div><div class='line' id='LC91'>	<span class="o">.</span><span class="na">in</span><span class="o">(</span><span class="s1">&#39;IS_AST_PARENT&#39;</span><span class="o">)</span></div><div class='line' id='LC92'>	<span class="o">.</span><span class="na">out</span><span class="o">(</span><span class="s1">&#39;USE&#39;</span><span class="o">)</span></div><div class='line' id='LC93'>	<span class="o">.</span><span class="na">filter</span><span class="o">{</span> <span class="n">it</span><span class="o">.</span><span class="na">code</span> <span class="o">!=</span> <span class="s2">&quot;&quot;</span> <span class="o">}</span></div><div class='line' id='LC94'><span class="o">});</span></div></pre></div></td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.06604s from github-fe133-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

