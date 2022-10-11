d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,0)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)

d.end()
