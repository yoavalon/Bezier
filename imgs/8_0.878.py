d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)

d.end()
