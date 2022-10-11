d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,3)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()
