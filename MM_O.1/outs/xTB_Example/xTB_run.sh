# -------Add Slurm setting here !!--------
module purge
module load xtb
xtb ../outs/xTB_Example/xyz/1.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/1.xyz
mv xtbopt.xyz out/xyz/1.xyz
xtb ../outs/xTB_Example/xyz/2.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/2.xyz
mv xtbopt.xyz out/xyz/2.xyz
xtb ../outs/xTB_Example/xyz/3.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/3.xyz
mv xtbopt.xyz out/xyz/3.xyz
xtb ../outs/xTB_Example/xyz/4.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/4.xyz
mv xtbopt.xyz out/xyz/4.xyz
xtb ../outs/xTB_Example/xyz/5.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/5.xyz
mv xtbopt.xyz out/xyz/5.xyz
xtb ../outs/xTB_Example/xyz/6.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/6.xyz
mv xtbopt.xyz out/xyz/6.xyz
xtb ../outs/xTB_Example/xyz/7.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/7.xyz
mv xtbopt.xyz out/xyz/7.xyz
xtb ../outs/xTB_Example/xyz/8.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/8.xyz
mv xtbopt.xyz out/xyz/8.xyz
xtb ../outs/xTB_Example/xyz/9.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/9.xyz
mv xtbopt.xyz out/xyz/9.xyz
xtb ../outs/xTB_Example/xyz/10.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/10.xyz
mv xtbopt.xyz out/xyz/10.xyz
xtb ../outs/xTB_Example/xyz/11.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/11.xyz
mv xtbopt.xyz out/xyz/11.xyz
xtb ../outs/xTB_Example/xyz/12.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/12.xyz
mv xtbopt.xyz out/xyz/12.xyz
xtb ../outs/xTB_Example/xyz/13.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/13.xyz
mv xtbopt.xyz out/xyz/13.xyz
xtb ../outs/xTB_Example/xyz/14.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/14.xyz
mv xtbopt.xyz out/xyz/14.xyz
xtb ../outs/xTB_Example/xyz/15.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/15.xyz
mv xtbopt.xyz out/xyz/15.xyz
xtb ../outs/xTB_Example/xyz/16.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/16.xyz
mv xtbopt.xyz out/xyz/16.xyz
xtb ../outs/xTB_Example/xyz/17.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/17.xyz
mv xtbopt.xyz out/xyz/17.xyz
xtb ../outs/xTB_Example/xyz/18.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/18.xyz
mv xtbopt.xyz out/xyz/18.xyz
xtb ../outs/xTB_Example/xyz/19.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/19.xyz
mv xtbopt.xyz out/xyz/19.xyz
xtb ../outs/xTB_Example/xyz/20.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/20.xyz
mv xtbopt.xyz out/xyz/20.xyz
xtb ../outs/xTB_Example/xyz/21.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/21.xyz
mv xtbopt.xyz out/xyz/21.xyz
xtb ../outs/xTB_Example/xyz/22.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/22.xyz
mv xtbopt.xyz out/xyz/22.xyz
xtb ../outs/xTB_Example/xyz/23.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/23.xyz
mv xtbopt.xyz out/xyz/23.xyz
xtb ../outs/xTB_Example/xyz/24.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/24.xyz
mv xtbopt.xyz out/xyz/24.xyz
xtb ../outs/xTB_Example/xyz/25.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/25.xyz
mv xtbopt.xyz out/xyz/25.xyz
xtb ../outs/xTB_Example/xyz/26.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/26.xyz
mv xtbopt.xyz out/xyz/26.xyz
xtb ../outs/xTB_Example/xyz/27.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/27.xyz
mv xtbopt.xyz out/xyz/27.xyz
xtb ../outs/xTB_Example/xyz/28.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/28.xyz
mv xtbopt.xyz out/xyz/28.xyz
xtb ../outs/xTB_Example/xyz/29.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/29.xyz
mv xtbopt.xyz out/xyz/29.xyz
xtb ../outs/xTB_Example/xyz/30.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/30.xyz
mv xtbopt.xyz out/xyz/30.xyz
xtb ../outs/xTB_Example/xyz/31.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/31.xyz
mv xtbopt.xyz out/xyz/31.xyz
xtb ../outs/xTB_Example/xyz/32.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/32.xyz
mv xtbopt.xyz out/xyz/32.xyz
xtb ../outs/xTB_Example/xyz/33.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/33.xyz
mv xtbopt.xyz out/xyz/33.xyz
xtb ../outs/xTB_Example/xyz/34.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/34.xyz
mv xtbopt.xyz out/xyz/34.xyz
xtb ../outs/xTB_Example/xyz/35.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/35.xyz
mv xtbopt.xyz out/xyz/35.xyz
xtb ../outs/xTB_Example/xyz/36.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/36.xyz
mv xtbopt.xyz out/xyz/36.xyz
xtb ../outs/xTB_Example/xyz/37.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/37.xyz
mv xtbopt.xyz out/xyz/37.xyz
xtb ../outs/xTB_Example/xyz/38.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/38.xyz
mv xtbopt.xyz out/xyz/38.xyz
xtb ../outs/xTB_Example/xyz/39.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/39.xyz
mv xtbopt.xyz out/xyz/39.xyz
xtb ../outs/xTB_Example/xyz/40.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/40.xyz
mv xtbopt.xyz out/xyz/40.xyz
xtb ../outs/xTB_Example/xyz/41.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/41.xyz
mv xtbopt.xyz out/xyz/41.xyz
xtb ../outs/xTB_Example/xyz/42.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/42.xyz
mv xtbopt.xyz out/xyz/42.xyz
xtb ../outs/xTB_Example/xyz/43.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/43.xyz
mv xtbopt.xyz out/xyz/43.xyz
xtb ../outs/xTB_Example/xyz/44.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/44.xyz
mv xtbopt.xyz out/xyz/44.xyz
xtb ../outs/xTB_Example/xyz/45.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/45.xyz
mv xtbopt.xyz out/xyz/45.xyz
xtb ../outs/xTB_Example/xyz/46.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/46.xyz
mv xtbopt.xyz out/xyz/46.xyz
xtb ../outs/xTB_Example/xyz/47.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/47.xyz
mv xtbopt.xyz out/xyz/47.xyz
xtb ../outs/xTB_Example/xyz/48.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/48.xyz
mv xtbopt.xyz out/xyz/48.xyz
xtb ../outs/xTB_Example/xyz/49.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/49.xyz
mv xtbopt.xyz out/xyz/49.xyz
xtb ../outs/xTB_Example/xyz/50.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/50.xyz
mv xtbopt.xyz out/xyz/50.xyz
xtb ../outs/xTB_Example/xyz/51.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/51.xyz
mv xtbopt.xyz out/xyz/51.xyz
xtb ../outs/xTB_Example/xyz/52.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/52.xyz
mv xtbopt.xyz out/xyz/52.xyz
xtb ../outs/xTB_Example/xyz/53.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/53.xyz
mv xtbopt.xyz out/xyz/53.xyz
xtb ../outs/xTB_Example/xyz/54.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/54.xyz
mv xtbopt.xyz out/xyz/54.xyz
xtb ../outs/xTB_Example/xyz/55.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/55.xyz
mv xtbopt.xyz out/xyz/55.xyz
xtb ../outs/xTB_Example/xyz/56.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/56.xyz
mv xtbopt.xyz out/xyz/56.xyz
xtb ../outs/xTB_Example/xyz/57.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/57.xyz
mv xtbopt.xyz out/xyz/57.xyz
xtb ../outs/xTB_Example/xyz/58.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/58.xyz
mv xtbopt.xyz out/xyz/58.xyz
xtb ../outs/xTB_Example/xyz/59.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/59.xyz
mv xtbopt.xyz out/xyz/59.xyz
xtb ../outs/xTB_Example/xyz/60.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/60.xyz
mv xtbopt.xyz out/xyz/60.xyz
xtb ../outs/xTB_Example/xyz/61.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/61.xyz
mv xtbopt.xyz out/xyz/61.xyz
xtb ../outs/xTB_Example/xyz/62.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/62.xyz
mv xtbopt.xyz out/xyz/62.xyz
xtb ../outs/xTB_Example/xyz/63.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/63.xyz
mv xtbopt.xyz out/xyz/63.xyz
xtb ../outs/xTB_Example/xyz/64.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/64.xyz
mv xtbopt.xyz out/xyz/64.xyz
xtb ../outs/xTB_Example/xyz/65.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/65.xyz
mv xtbopt.xyz out/xyz/65.xyz
xtb ../outs/xTB_Example/xyz/66.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/66.xyz
mv xtbopt.xyz out/xyz/66.xyz
xtb ../outs/xTB_Example/xyz/67.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/67.xyz
mv xtbopt.xyz out/xyz/67.xyz
xtb ../outs/xTB_Example/xyz/68.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/68.xyz
mv xtbopt.xyz out/xyz/68.xyz
xtb ../outs/xTB_Example/xyz/69.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/69.xyz
mv xtbopt.xyz out/xyz/69.xyz
xtb ../outs/xTB_Example/xyz/70.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/70.xyz
mv xtbopt.xyz out/xyz/70.xyz
xtb ../outs/xTB_Example/xyz/71.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/71.xyz
mv xtbopt.xyz out/xyz/71.xyz
xtb ../outs/xTB_Example/xyz/72.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/72.xyz
mv xtbopt.xyz out/xyz/72.xyz
xtb ../outs/xTB_Example/xyz/73.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/73.xyz
mv xtbopt.xyz out/xyz/73.xyz
xtb ../outs/xTB_Example/xyz/74.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/74.xyz
mv xtbopt.xyz out/xyz/74.xyz
xtb ../outs/xTB_Example/xyz/75.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/75.xyz
mv xtbopt.xyz out/xyz/75.xyz
xtb ../outs/xTB_Example/xyz/76.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/76.xyz
mv xtbopt.xyz out/xyz/76.xyz
xtb ../outs/xTB_Example/xyz/77.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/77.xyz
mv xtbopt.xyz out/xyz/77.xyz
xtb ../outs/xTB_Example/xyz/78.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/78.xyz
mv xtbopt.xyz out/xyz/78.xyz
xtb ../outs/xTB_Example/xyz/79.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/79.xyz
mv xtbopt.xyz out/xyz/79.xyz
xtb ../outs/xTB_Example/xyz/80.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/80.xyz
mv xtbopt.xyz out/xyz/80.xyz
xtb ../outs/xTB_Example/xyz/81.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/81.xyz
mv xtbopt.xyz out/xyz/81.xyz
xtb ../outs/xTB_Example/xyz/82.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/82.xyz
mv xtbopt.xyz out/xyz/82.xyz
xtb ../outs/xTB_Example/xyz/83.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/83.xyz
mv xtbopt.xyz out/xyz/83.xyz
xtb ../outs/xTB_Example/xyz/84.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/84.xyz
mv xtbopt.xyz out/xyz/84.xyz
xtb ../outs/xTB_Example/xyz/85.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/85.xyz
mv xtbopt.xyz out/xyz/85.xyz
xtb ../outs/xTB_Example/xyz/86.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/86.xyz
mv xtbopt.xyz out/xyz/86.xyz
xtb ../outs/xTB_Example/xyz/87.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/87.xyz
mv xtbopt.xyz out/xyz/87.xyz
xtb ../outs/xTB_Example/xyz/88.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/88.xyz
mv xtbopt.xyz out/xyz/88.xyz
xtb ../outs/xTB_Example/xyz/89.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/89.xyz
mv xtbopt.xyz out/xyz/89.xyz
xtb ../outs/xTB_Example/xyz/90.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/90.xyz
mv xtbopt.xyz out/xyz/90.xyz
xtb ../outs/xTB_Example/xyz/91.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/91.xyz
mv xtbopt.xyz out/xyz/91.xyz
xtb ../outs/xTB_Example/xyz/92.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/92.xyz
mv xtbopt.xyz out/xyz/92.xyz
xtb ../outs/xTB_Example/xyz/93.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/93.xyz
mv xtbopt.xyz out/xyz/93.xyz
xtb ../outs/xTB_Example/xyz/94.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/94.xyz
mv xtbopt.xyz out/xyz/94.xyz
xtb ../outs/xTB_Example/xyz/95.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/95.xyz
mv xtbopt.xyz out/xyz/95.xyz
xtb ../outs/xTB_Example/xyz/96.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/96.xyz
mv xtbopt.xyz out/xyz/96.xyz
xtb ../outs/xTB_Example/xyz/97.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/97.xyz
mv xtbopt.xyz out/xyz/97.xyz
xtb ../outs/xTB_Example/xyz/98.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/98.xyz
mv xtbopt.xyz out/xyz/98.xyz
xtb ../outs/xTB_Example/xyz/99.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/99.xyz
mv xtbopt.xyz out/xyz/99.xyz
xtb ../outs/xTB_Example/xyz/100.xyz --opt tight --cycles 3000 --charge 0
rm xtbrestart xtbtopo.mol wbo charges
mv xtbopt.log out/log/100.xyz
mv xtbopt.xyz out/xyz/100.xyz
