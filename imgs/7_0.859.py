d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.N, Length.medium)
d.position_pen(0,0)
d.straight_line(Direction.S, Length.medium)

d.end()
