import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		boolean array[][] = new boolean[10][10];
		for (int i = 0; i < 10; i++) {
			String str = br.readLine();
			for (int j = 0; j < 10; j++) {
				if (str.charAt(j) == '1') {
					array[i][j] = true;
				} else {
					array[i][j] = false;
				}
			}
		}
		calc(array);
	}

	public static void fail() { // 직각이등변삼각형이 아닌 경우
		System.out.println(0);
	}

	public static void success(int point[][]) { // 직각이등변삼각형일 경우
		// 0,0부터 시작했으나, 문제 기준은 1,1이니 각각 1을 더해준다.
		for (int i = 0; i < 3; i++) {
			System.out.println((point[i][0] + 1) + " " + (point[i][1] + 1));
		}
	}

	public static void calc(boolean array[][]) {
		// 삼각형 타입 1(x,y축에 평행한 두 변) or 2(x,y축에 평행한 한 변)
		int type = 0;

		// 이론상으로 꼭짓점은 3개
		int point[][] = new int[3][2];
		int p = 0; // 꼭짓점 개수

		int dr[] = { -1, 1, 0, 0 };
		int dc[] = { 0, 0, -1, 1 };

		// type 2 꼭짓점 3개
				//10000
				//11000
				//11100
				//11000
				//10000
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (array[i][j] == true) {
					// 상하좌우 중 3군데 이상이 전부 0이거나 배열 밖이라면, 이는 type 2의 꼭짓점
					int count = 0;
					for (int k = 0; k < 4; k++) {
						int nextX = i + dr[k];
						int nextY = j + dc[k];
						if ((nextX < 0) || (nextX >= 10) || (nextY < 0) || (nextY >= 10)) { // 범위 밖
							count++;
						} else if (array[nextX][nextY] == false) { // 주변이 0인 경우 count++
							count++;
						}
					}
					if (count >= 3) { // 꼭짓점인 경우
						if (p >= 3) { // 꼭짓점 개수가 3개 초과 -> 삼각형 아님
							fail();
							return;
						}
						point[p][0] = i;
						point[p][1] = j;
						p++;
						if (p == 3) { // type 2일 때 꼭짓점
							type = 2; 
						}
					}
				}
			}
		}
		// type 1 꼭짓점 2개 -> 해당 교차지점(직각꼭짓점) 두 곳 봐야 함
			//111
			//110
			//100
		if (p == 2) {
			type = 1;
			if (array[point[0][0]][point[1][1]]) {
				int count = 0;
				for (int k = 0; k < 4; k++) {
					int nextX = point[0][0] + dr[k];
					int nextY = point[1][1] + dc[k];
					if ((nextX < 0) || (nextX >= 10) || (nextY < 0) || (nextY >= 10)) {
						count++;
					} else if (array[nextX][nextY] == false) {
						count++;
					}
				}
				if (count >= 2) { 
					point[p][0] = point[0][0];
					point[p][1] = point[1][1];
					p++;
				}
			} else if (array[point[1][0]][point[0][1]]) {
				int count = 0;
				for (int k = 0; k < 4; k++) {
					int nextX = point[1][0] + dr[k];
					int nextY = point[0][1] + dc[k];
					if ((nextX < 0) || (nextX >= 10) || (nextY < 0) || (nextY >= 10)) {
						count++;
					} else if (array[nextX][nextY] == false) {
						count++;
					}
				}
				if (count >= 2) {
					point[p][0] = point[1][0];
					point[p][1] = point[0][1];
					p++;
				}
			}

			// 재정렬
			Arrays.sort(point, new Comparator<int[]>() {
				@Override
				public int compare(int[] o1, int[] o2) {
					if (o1[0] == o2[0]) {
						return o1[1] - o2[1];
					} else {
						return o1[0] - o2[0];
					}
				}
			});

		}
		if (p != 3) {
			fail();
			return;
		}
		// 조건 2. 데이터 값이 삼각형 모양 안에 정확히 채워져있는지 확인
		boolean tempCheck[][] = new boolean[10][10];
		if (type == 1) {
			int direction = 0; // 세로로 같다면 1, 가로로 같다면 2
			int sameVal = 0;
			int difVal = 0;
			if (point[0][0] == point[1][0]) {
				if (point[0][1] == point[2][1]) {
					// 남은 꼭지점은 좌측 아래
					int length = point[1][1] - point[0][1];
					for (int i = point[0][0]; i <= point[2][0]; i++) {
						for (int j = 0; j <= length; j++) {
							tempCheck[i][point[0][1] + j] = true;
						}
						length -= 1;
					}
				} else {
					// 남은 꼭지점은 우측 아래
					int length = point[1][1] - point[0][1];
					for (int i = point[0][0]; i <= point[2][0]; i++) {
						for (int j = 0; j <= length; j++) {
							tempCheck[i][point[1][1] - j] = true;
						}
						length -= 1;
					}
				}
			} else if (point[1][0] == point[2][0]) {
				if (point[0][1] == point[1][1]) {
					// 남은 꼭지점은 좌측 위
					int length = point[2][1] - point[1][1];
					for (int i = point[2][0]; i >= point[0][0]; i--) {
						for (int j = 0; j <= length; j++) {
							tempCheck[i][point[1][1] + j] = true;
						}
						length -= 1;
					}
				} else {
					// 남은 꼭지점은 우측 위
					int length = point[2][1] - point[1][1];
					for (int i = point[2][0]; i >= point[0][0]; i--) {
						for (int j = 0; j <= length; j++) {
							tempCheck[i][point[2][1] - j] = true;
						}
						length -= 1;
					}
				}
			}
		} else if (type == 2) {
			int direction = 0; // 세로로 같다면 1, 가로로 같다면 2
			int sameVal = 0;
			int difVal = 0;
			// 세로로 같은지 가로로 같은지 확인
			if (point[0][1] == point[1][1]) {
				direction = 1;
				sameVal = 0;
				difVal = 2;
			} else if (point[0][1] == point[2][1]) {
				direction = 1;
				sameVal = 0;
				difVal = 1;
			} else if (point[0][0] == point[1][0]) {
				direction = 2;
				sameVal = 0;
				difVal = 2;
			} else if (point[1][0] == point[2][0]) {
				direction = 2;
				sameVal = 1;
				difVal = 0;
			}
			// 세로로 같다면
			if (direction == 1) {
				// 좌에서 우로 탐방하는가?
				if (point[sameVal][1] < point[difVal][1]) {
					int length = Math.abs(point[sameVal][0] - point[3 - sameVal - difVal][0]);
					for (int i = point[sameVal][1]; i <= point[difVal][1]; i++) {
						for (int j = 0; j <= length; j++) {
							tempCheck[(i - point[sameVal][1]) + j
									+ Math.min(point[sameVal][0], point[3 - sameVal - difVal][0])][i] = true;
						}
						length -= 2;
					}
				}
				// 우에서 좌로 탐방하는가?
				else {
					int length = Math.abs(point[sameVal][0] - point[3 - sameVal - difVal][0]);
					for (int i = point[sameVal][1]; i >= point[difVal][1]; i--) {
						for (int j = 0; j <= length; j++) {
//							System.out.print("length : " + length + ", ");
//							System.out.println((i-point[sameVal][1]) + j+Math.min(point[sameVal][0], point[3-sameVal-difVal][0]));
							tempCheck[(point[sameVal][1] - i) + j
									+ Math.min(point[sameVal][0], point[3 - sameVal - difVal][0])][i] = true;
						}
						length -= 2;
					}
				}
			}
			// 가로로 같다면
			else if (direction == 2) {
				// 위에서 아래로 탐방하는가?
				if (point[sameVal][0] < point[difVal][0]) {
					int length = Math.abs(point[sameVal][1] - point[3 - sameVal - difVal][1]);
					for (int i = point[sameVal][0]; i <= point[difVal][0]; i++) {
						for (int j = 0; j <= length; j++) {
							tempCheck[i][(i - point[sameVal][0]) + j
									+ Math.min(point[sameVal][1], point[3 - sameVal - difVal][1])] = true;
						}
						length -= 2;
					}
				}
				// 아래에서 위로 탐방하는가?
				else {
					int length = Math.abs(point[sameVal][1] - point[3 - sameVal - difVal][1]);
					for (int i = point[sameVal][0]; i >= point[difVal][0]; i--) {
						for (int j = 0; j <= length; j++) {
							tempCheck[i][(point[sameVal][0] - i) + j
									+ Math.min(point[sameVal][1], point[3 - sameVal - difVal][1])] = true;
						}
						length -= 2;
					}
				}
			} else {
				fail();
				return;
			}
		} else {
			fail();
			return;
		}
//		for (int i = 0; i < 10; i++) {
//			for (int j = 0; j < 10; j++) {
//				if (tempCheck[i][j]) {
//					System.out.print("1");
//				} else {
//					System.out.print("0");
//				}
//			}
//			System.out.println();
//		}
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (tempCheck[i][j] != array[i][j]) {
					fail();
					return;
				}
			}
		}

		double lengthA = Math.pow((point[0][0] - point[1][0]), 2) + Math.pow((point[0][1] - point[1][1]), 2);
		double lengthB = Math.pow((point[1][0] - point[2][0]), 2) + Math.pow((point[1][1] - point[2][1]), 2);
		double lengthC = Math.pow((point[0][0] - point[2][0]), 2) + Math.pow((point[0][1] - point[2][1]), 2);

		// 직각인지 확인
		if ((lengthC > lengthA) && (lengthC > lengthB)) {
			if (lengthC != lengthA + lengthB) {
				fail();
				return;
			}
		}
		if ((lengthB > lengthA) && (lengthB > lengthC)) {
			if (lengthB != lengthA + lengthC) {
				fail();
				return;
			}
		}
		if ((lengthA > lengthC) && (lengthA > lengthB)) {
			if (lengthA != lengthC + lengthB) {
				fail();
				return;
			}
		}

		// 이등변인지 확인
		if ((lengthC != lengthA) && (lengthB != lengthC) && (lengthA != lengthB)) {
			fail();
			return;
		}

		// 출력
		success(point);
		return;
	}
}