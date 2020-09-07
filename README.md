# UPT (Your Personal Training) _ 200907 ver.
* 광주 인공지능 사관학교 워밍업 프로젝트<br>
* 팀장 : 박지현 <br>
* 팀원 : 박성철 윤경지 전주현 <br>
* 팀플 규칙 : 자신의 이름(이니셜, 닉네임)로 branch명을 작성해주시고, 하나의 폴더를 업데이트하는 방식을 취해주세요. (단일 파일 X)
<br>

## 프로젝트 개요
언택트 시대인 요즘, 유튜브를 보면 하는 홈트레이닝에 PT를 해주는 AI가 있다!<br>
UPT. 당신의 건강의 시작이 되도록.
<br>

## 주요 기술
* Google API POSNET
* WEB ( HTML, CSS, JS)
<br>

## 참고 링크 모음
* [posenet 기본 개념](https://medium.com/tensorflow/real-time-human-pose-estimation-in-the-browser-with-tensorflow-js-7dd0bc881cd5)
* [메인으로 사용할 posenet의 github](https://github.com/tensorflow/tfjs-models/tree/master/posenet)
* [혹시 처음할 때 Uncaught (in promise) DOMException 에러가 뜬다면 참고하세요](https://stackoverflow.com/questions/59577407/uncaught-in-promise-domexception-failed-to-execute-teximage2d-on-webgl2ren)
* [웹으로 posenet을 구현한 또다른 github(비추)](http://blog.naver.com/PostView.nhn?blogId=tramper2&logNo=221834379945&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)
<br>

## (영어가 힘드신 분) [posenet 기본 개념](https://medium.com/tensorflow/real-time-human-pose-estimation-in-the-browser-with-tensorflow-js-7dd0bc881cd5) 를 제 나름대로 해석한 것입니다.
#### [0] 배경 지식

한 사람, 여러 사람 ver이 있는데, 한 사람이 더 빠르고 간단하다. 근데 진짜 한 사람밖에 못한다.
-> 우리는 우선은 한 사람만으로 한정하도록 하자.

1. 이미지를 CNN에 넣는다
2. single_pose or multi_pose 해석 알고리즘이 모델에서 poses, pose confidence scores, keypoint positions, and keypoint confidence scores을 추출한다.

* Pose - keypoint list 를 포함한 pose object, 신뢰도
* Pose confidence score - 0~1까지의 값. 포즈 추정의 신뢰도를 나타낸다.정확하지 않아보이는 포즈를 숨기는데 활용 가능
* Keypoint - 현재 17가지 keypoint를 잡아낼 수 있고, postion, keypoint 신뢰도를 포함한다.
* Keypoint confidence score - Pose confidence score와 거의 유사하나 keypoint에 대한 것.
* Keypoint position - 2D로 원본 input이미지에서의 keypoint의 x, y위치

### [1] TensorFlow.js, PoseNet 라이브러리 설치하기
```html
<html>
  <body>
    <!-- Load TensorFlow.js -->
    <script src="https://unpkg.com/@tensorflow/tfjs"></script>
    <!-- Load Posenet -->
    <script src="https://unpkg.com/@tensorflow-models/posenet">
    </script>
    <script type="text/javascript">
      posenet.load().then(function(net) {
        // posenet model loaded
      });
    </script>
  </body>
</html>
```

### [2] single-pose estimation algorithm의 input
* Input image element : 우리가 posenet 적용시킬 이미지(동영상)의 html element (무조건 SQUARE여야!)
* Image scale factor : default는 0.5이고, 0.2~1 사이의 값이다. CNN돌리기 전에 이미지 크기 조정. 이 수가 낮을 수록 빠르다. (정확도는 내려간다.)
* Flip horizontal : default는 False이고, 수평적으로 flip이 필요하면 True로 바꿔라.(그러면 리턴에선 flip된 채로 나옴)
* Output stride : default는 16이고, 32, 16, 8 중에 하나여야 한다. 내부적으로는 CNN의 레이어의 높이, 너비에 영향을 준다.
                     유저단에서는 정확도와 속도에 영향을 준다. 낮으면 정확도는 올라가고 느려진다. 높으면 그 반대.


### [3] output
* pose confidence score, 17개의 keypoints를 포함한 pose
* 각 keypoint는 keypoint position(원본 이미지와 바로 연결), keypoint confidence score를 포함. 
<br>

## (영어가 힘드신 분) [메인으로 사용할 posenet의 github](https://github.com/tensorflow/tfjs-models/tree/master/posenet) 를 제 나름대로 해석한 것입니다.
* outputStride : 클수록 빠르고 정확도 내려감
* inputResolution : 작을수록 빠르고 정확도 내려감
* multiplier : MobileNet에서만 사용된다. Resnet에서는 사용 안함. 작을수록 빠르고 정확도 내려감
* quantBytes : 작을수록 정확도 내려가고 용량도 줄음
* modelUrl : 옵션. model의 URL을 명시하고 싶을 때. local한 개발할 때 사용
***
+ 디폴트는 MobileNet에 0.75 multiplier
+ 모바일에서는 0.5 multiplier가 적당
+ ResNet은 강력한 GPU 있는 컴에서 추천합니다.


