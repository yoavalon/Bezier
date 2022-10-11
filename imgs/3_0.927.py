d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)

d.end()
