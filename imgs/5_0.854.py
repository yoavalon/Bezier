d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
