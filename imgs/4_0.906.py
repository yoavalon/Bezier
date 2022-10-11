d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)

d.end()
