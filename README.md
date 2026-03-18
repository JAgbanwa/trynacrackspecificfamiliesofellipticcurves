# trynacrackspecificfamiliesofellipticcurves

\begin{equation}\label{1.3}
   v^2 = X^3 + \left(-\frac{1}{3} \cdot m^4 + \frac{1}{3} \cdot m^3\right) \cdot X 
+ \frac{2}{27} \cdot m^6 - \frac{1}{9} \cdot m^5 + \frac{1}{36} \cdot m^4 - \frac{19}{36} \cdot m \quad \text{where $X = x - \dfrac{m^2}{3}$}
\end{equation}
The part of equation \eqref{1.3} 
\begin{align*}
    u &= \frac{2}{27} \cdot m^6 - \frac{1}{9} \cdot m^5 + \frac{1}{36} \cdot m^4 - \frac{19}{36} \cdot m \\
    u &= \dfrac{72m^6 - 108m^5 + 27m^4 - 513m}{972}
\end{align*}

has the following families as solutions:

\renewcommand{\arraystretch}{2.2}
\begin{table}[H]
\centering
\caption{Complete list of integer solution families}
\label{tab:solutions}
\begin{tabular}{c p{2.2cm} p{10.5cm}}
\toprule
\textbf{\#} & \textbf{$m(n)$} & \textbf{$u(n)$} \\
\midrule
1 & $108 \cdot n$ & $3\cdot\left(39182082048\,n^6 - 544195584\,n^5 + 1259712\,n^4 - 19\,n\right)$ \\

2 & $36 \cdot (3n+1)$ & $117546246144n^6 + 233459905536n^5 + 193193211456n^4$
+ $85262347008n^3 + 21165681024\,n^2 + 2802159303\,n + 154571309$ \\

3 &
$36 \cdot (3n+2)$ &
$117546246144n^6 + 468552397824n^5 + 778203464256n^4$
$+ 689324484096n^3 + 343457957376n^2 + 91268093895n + 10105316314$ \\

4 &
$27 \cdot (4n+1)$ & 
$3 \cdot \left(39182082048n^6 + 58228927488n^5 + 36054217152n^4 \right.$ + $\left.11905538112n^3 + 2211266952n^2 + 219032405n + 9039413\right)$ \\

5 &
$9 \cdot (12n+7)$ &
$117546246144n^6 + 409779274752n^5 + 595217699136n^4$
$+ 461101201344n^3 + 200925481176n^2 + 46694776911n + 4521537356$ \\

6 &
$9 \cdot (12n+11)$ &
$117546246144n^6 + 644871767040n^5 + 1474093567296n^4$
$+ 1797106398912n^3 + 1232376407064n^2 + 450723291423n + 68685282985$ \\

\bottomrule
\end{tabular}
\end{table}
