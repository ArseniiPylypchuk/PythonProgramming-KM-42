import re
def points_scores(pose_estimation):
    pattern= re.compile(r"BodyPart:\d+-\(([\d.]+), ([\d.]+)\) score=([\d.]+)")
    points =[]
    scores= []
    matches= pattern.findall(pose_estimation)
    for i in matches:
        x, y, score= i
        points.extend([x, y])
        scores.append(score)
    return points, scores
pose_estimation= """[BodyPart:0-(0.48, 0.16) score=0.91 BodyPart:1-(0.50, 0.27) score=0.85 BodyPart:2-(0.44, 0.27) score=0.74 BodyPart:3-(0.37, 0.26) score=0.71 BodyPart:4-(0.30, 0.23) score=0.79 BodyPart:5-(0.56, 0.28) score=0.76 BodyPart:6-(0.66, 0.29) score=0.82 BodyPart:7-(0.76, 0.29) score=0.74 BodyPart:8-(0.45, 0.42) score=0.68 BodyPart:11-(0.51, 0.45) score=0.70 BodyPart:12-(0.49, 0.59) score=0.86 BodyPart:13-(0.47, 0.74) score=0.88 BodyPart:14-(0.47, 0.15) score=0.67 BodyPart:15-(0.49, 0.16) score=0.94 BodyPart:17-(0.52, 0.18) score=0.96]"""
points, scores= points_scores(pose_estimation)
print("points =", points)
print("scores=", scores)
