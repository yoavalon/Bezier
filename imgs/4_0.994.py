d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)

d.end()
