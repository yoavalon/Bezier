d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.position_pen(1,3)

d.end()
