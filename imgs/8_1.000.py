d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
