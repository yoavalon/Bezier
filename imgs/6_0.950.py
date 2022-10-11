d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)

d.end()
