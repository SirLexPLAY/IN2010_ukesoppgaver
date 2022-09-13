\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{in1150-innlevering}[2018/09/14 Innlevering for IN1150 -- Logiske metoder]
\LoadClass[12pt,norsk,a4paper]{article}

% Språk og tegn
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[norsk]{babel}
\RequirePackage{tikz}

% Fonter
\RequirePackage{tgpagella}
\RequirePackage[small,euler-digits]{eulervm}

% Lister
\RequirePackage{enumitem}
\newlist{deloppgaver}{enumerate}{1}
\setlist[deloppgaver]{label={\textbf{(\alph*)}},leftmargin=*}

% Matematikk
\RequirePackage{amsmath,amssymb}

% Noen nyttige forkortelser
\newcommand{\set}[1]{\ensuremath{\{#1\}}}
\newcommand{\tuple}[1]{\ensuremath{\langle #1 \rangle}}
\newcommand{\imp}{\ensuremath{\rightarrow}}
\newcommand{\union}{\ensuremath{\cup}}
\newcommand{\snitt}{\ensuremath{\cap}}
\newcommand{\str}[1]{\textcolor{blue}{\normalfont\texttt{#1}}}


% Større kommentarer
\RequirePackage{verbatim}
\usepackage{hyperref}
