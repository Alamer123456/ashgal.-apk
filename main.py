<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>لعبة X و O</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .cell {
            transition: all 0.3s ease;
        }
        .cell:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        .winning-cell {
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { background-color: rgba(134, 239, 172, 0.5); }
            50% { background-color: rgba(134, 239, 172, 0.8); }
            100% { background-color: rgba(134, 239, 172, 0.5); }
        }
        .draw-cell {
            animation: drawPulse 1.5s infinite;
        }
        @keyframes drawPulse {
            0% { background-color: rgba(209, 213, 219, 0.5); }
            50% { background-color: rgba(209, 213, 219, 0.8); }
            100% { background-color: rgba(209, 213, 219, 0.5); }
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col items-center justify-center font-sans">
    <div class="container mx-auto px-4 py-8">
        <h1 class="text-4xl md:text-5xl font-bold text-center text-indigo-700 mb-6">لعبة X و O</h1>
        
        <div class="bg-white rounded-xl shadow        <div class="bg-white rounded-xl shadow-2xl p-6 max-w-md mx-auto">
            -2xl p-6 max-w-md mx-auto">
            <!-- معلومات اللاعبين -->
            <div class="flex justify-between items-center mb-6">
                <div id="player1" class="flex items-center bg-blue-100 px-4 py-2 rounded-lg">
                    <i class="fas fa-user text-blue-600 ml-2"></i>
                    <span class="font-semibold text-blue-800">اللاعب X</span>
                    <span id="score1" class="bg-blue-600 text-white rounded-full w-6 h-6 flex items-center justify-center text-sm mr-2">0</span>
                </div>
                
                <div class="text-gray-500 font-medium">VS</div>
                
                <div id="player2" class="flex items-center bg-red-100 px-4 py-2 rounded-lg">
                    <i class="fas fa-user text-red-600 ml-2"></i>
                    <span class="font-semibold text-red-800">اللاعب O</span>
                    <span id="score2" class="bg-red-600 text-white rounded-full w-6 h-6 flex items-center justify-center text-sm mr-2">0</span>
                </div>
            </div>
            
            <!-- لوحة اللعبة -->
            <div class="grid grid-cols-3 gap-3 mb-6">
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="0"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="1"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="2"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="3"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="4"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="5"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="6"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="7"></div>
                <div class="cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200" data-index="8"></div>
            </div>
            
            <!-- حالة اللعبة -->
            <div id="status" class="text-center text-lg font-semibold mb-6 text-indigo-600">دور اللاعب X</div>
            
            <!-- أزرار التحكم -->
            <div class="flex justify-center space-x-4">
                <button id="restartBtn" class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg transition">
                    <i class="fas fa-sync-alt ml-2"></i> إعادة اللعب
                </button>
                <button id="resetScoreBtn" class="bg-gray-600 hover:bg-gray-700 text-white px-4 py-2 rounded-lg transition">
                    <i class="fas fa-trash-alt ml-2"></i> إعادة النقاط
                </button>
            </div>
        </div>
        
        <!-- تعليمات اللعبة -->
        <div class="mt-8 bg-white rounded-xl shadow-lg p-6 max-w-md mx-auto">
            <h2 class="text-xl font-bold text-gray-800 mb-4">تعليمات اللعبة:</h2>
            <ul class="list-disc pr-5 text-gray-700 space-y-2">
                <li>اللاعب الأول (X) يبدأ اللعب دائمًا</li>
                <li>اضغط على أي مربع فارغ لوضع علامتك</li>
                <li>الهدف هو تكوين صف من 3 علامات متشابهة (أفقي أو رأسي أو قطري)</li>
                <li>إذا امتلأت جميع المربعات دون فائز، تكون النتيجة تعادل</li>
            </ul>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // حالة اللعبة
            const state = {
                board: Array(9).fill(''),
                currentPlayer: 'X',
                gameOver: false,
                scores: { X: 0, O: 0 }
            };
            
            // عناصر DOM
            const cells = document.querySelectorAll('.cell');
            const statusElement = document.getElementById('status');
            const score1Element = document.getElementById('score1');
            const score2Element = document.getElementById('score2');
            const player1Element = document.getElementById('player1');
            const player2Element = document.getElementById('player2');
            const restartBtn = document.getElementById('restartBtn');
            const resetScoreBtn = document.getElementById('resetScoreBtn');
            
            // تهيئة اللعبة
            initGame();
            
            // إضافة مستمعي الأحداث
            cells.forEach(cell => {
                cell.addEventListener('click', handleCellClick);
            });
            
            restartBtn.addEventListener('click', restartGame);
            resetScoreBtn.addEventListener('click', resetScores);
            
            // وظائف اللعبة
            function initGame() {
                state.board = Array(9).fill('');
                state.currentPlayer = 'X';
                state.gameOver = false;
                
                updateUI();
            }
            
            function handleCellClick(e) {
                if (state.gameOver) return;
                
                const index = parseInt(e.target.dataset.index);
                
                if (state.board[index] !== '') return;
                
                state.board[index] = state.currentPlayer;
                e.target.textContent = state.currentPlayer;
                
                // إضافة لون للعلامة
                if (state.currentPlayer === 'X') {
                    e.target.classList.add('text-blue-600');
                } else {
                    e.target.classList.add('text-red-600');
                }
                
                // التحقق من الفوز
                const winner = checkWinner();
                if (winner) {
                    handleGameEnd(winner);
                    return;
                }
                
                // التحقق من التعادل
                if (isBoardFull()) {
                    handleGameEnd(null);
                    return;
                }
                
                // تبديل اللاعب
                state.currentPlayer = state.currentPlayer === 'X' ? 'O' : 'X';
                updateUI();
            }
            
            function checkWinner() {
                const winPatterns = [
                    [0, 1, 2], [3, 4, 5], [6, 7, 8], // صفوف
                    [0, 3, 6], [1, 4, 7], [2, 5, 8], // أعمدة
                    [0, 4, 8], [2, 4, 6]             // أقطار
                ];
                
                for (const pattern of winPatterns) {
                    const [a, b, c] = pattern;
                    if (state.board[a] && state.board[a] === state.board[b] && state.board[a] === state.board[c]) {
                        return state.board[a];
                    }
                }
                
                return null;
            }
            
            function isBoardFull() {
                return state.board.every(cell => cell !== '');
            }
            
            function handleGameEnd(winner) {
                state.gameOver = true;
                
                if (winner) {
                    // تحديث النقاط
                    state.scores[winner]++;
                    
                    // عرض الفائز
                    statusElement.textContent = `فاز اللاعب ${winner}!`;
                    statusElement.classList.add('text-green-600');
                    
                    // إبراز الخلايا الفائزة
                    highlightWinningCells(winner);
                    
                    // تحديث عرض النقاط
                    updateScores();
                } else {
                    statusElement.textContent = 'تعادل!';
                    statusElement.classList.add('text-gray-600');
                    
                    // إبراز جميع الخلايا في حالة التعادل
                    cells.forEach(cell => {
                        cell.classList.add('draw-cell');
                    });
                }
            }
            
            function highlightWinningCells(winner) {
                const winPatterns = [
                    [0, 1, 2], [3, 4, 5], [6, 7, 8], // صفوف
                    [0, 3, 6], [1, 4, 7], [2, 5, 8], // أعمدة
                    [0, 4, 8], [2, 4, 6]             // أقطار
                ];
                
                for (const pattern of winPatterns) {
                    const [a, b, c] = pattern;
                    if (state.board[a] === winner && state.board[a] === state.board[b] && state.board[a] === state.board[c]) {
                        cells[a].classList.add('winning-cell');
                        cells[b].classList.add('winning-cell');
                        cells[c].classList.add('winning-cell');
                        break;
                    }
                }
            }
            
            function updateUI() {
                // تحديث حالة اللعبة
                statusElement.textContent = `دور اللاعب ${state.currentPlayer}`;
                statusElement.className = 'text-center text-lg font-semibold mb-6 text-indigo-600';
                
                // تحديث تمييز اللاعب الحالي
                if (state.currentPlayer === 'X') {
                    player1Element.classList.add('ring-2', 'ring-blue-500');
                    player2Element.classList.remove('ring-2', 'ring-red-500');
                } else {
                    player2Element.classList.add('ring-2', 'ring-red-500');
                    player1Element.classList.remove('ring-2', 'ring-blue-500');
                }
                
                // تحديث الخلايا
                cells.forEach((cell, index) => {
                    cell.textContent = state.board[index];
                    cell.className = 'cell bg-gray-50 rounded-lg h-24 md:h-28 flex items-center justify-center text-4xl font-bold cursor-pointer border-2 border-gray-200';
                    
                    if (state.board[index] === 'X') {
                        cell.classList.add('text-blue-600');
                    } else if (state.board[index] === 'O') {
                        cell.classList.add('text-red-600');
                    }
                });
            }
            
            function updateScores() {
                score1Element.textContent = state.scores.X;
                score2Element.textContent = state.scores.O;
            }
            
            function restartGame() {
                // إزالة التمييز من الخلايا
                cells.forEach(cell => {
                    cell.classList.remove('winning-cell', 'draw-cell');
                });
                
                initGame();
            }
            
            function resetScores() {
                state.scores = { X: 0, O: 0 };
                updateScores();
                restartGame();
            }
        });
    </script>
</body>
</html>
