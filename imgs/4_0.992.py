d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
