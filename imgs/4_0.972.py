d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,3)

d.end()
